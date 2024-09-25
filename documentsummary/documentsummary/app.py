from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
import PyPDF2
import docx

# import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import string

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')


def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Calculate word frequency
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    word_frequencies = defaultdict(int)
    for word in word_tokenize(text.lower()):
        if word not in stop_words:
            word_frequencies[word] += 1

    # Score sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if len(sentence.split(' ')) < 30:  # Ignore long sentences
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Sort sentences by score and return the top N sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(summarized_sentences)
    return summary

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def summarize_pdf(pdf_path):
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Summarize the extracted text
    summary = summarize_text(text)
    
    return summary

def allowed_file(filename):
    #return True
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'docx', 'txt', ''}

def extract_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['document']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Process the document here and generate summary
        _, file_extension = os.path.splitext(filepath)
        summary = ''
        if file_extension == '.docx':
            summary = summarize_text(extract_text_from_docx(filepath))
        elif file_extension == '.pdf':
            summary = summarize_pdf(filepath)
        elif file_extension == '.txt':
            summary = summarize_text(extract_text_from_txt(filepath))
        
        # Remove the file after processing
        os.remove(filepath)

        return jsonify({'summary': summary})
    
    return jsonify({'error': 'Invalid file type'}), 400