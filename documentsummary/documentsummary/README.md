# DOCUMENT SUMMARIZER

This project aims to develop a web application that allows users to upload documents in various formats such as docx,pdf,text etc. and receive concise summaries of their contents with the click of a button. By providing a user-friendly interface and robust backend processing, this application enhances productivity for users needing quick insights from lengthy documents.

# Requirement.txt

PyPDF
docx

pip install flask PyPDF2 python-docx nltk

# Methods
# Frontend
HTML: A simple form to facilitates file uploads, including a button to initiate the summarization process. HTML stands for Hypertext Markup Language and it's the code used to structure web pages and their content. HTML is the foundation of the web and tells web brewers how to display text, images, and other media on a page.

CSS:  Basic styling to enhance the user interface.CSS stands for Cascading Style Sheets. CSS describes how HTML elements are to be displayed on screen, paper, or in other media.CSS saves a lot of work. It can control the layout of multiple web pages all at once.

JS:  Fetch API to handle asynchronous requests to the Flask backend, allowing users to upload files and receive summaries without reloading the page.JavaScript is a scripting or programming language that allows you to implement complex features on web pages ,every time a web page does more than just sit there and display static information for you to look at , displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. . It is the third layer of the layer cake of standard web technologies, two of which (HTML and CSS) we have covered in much more detail in other parts of the Learning Area.

# Backend
Flask: A lightweight web framework used to create an API for handling file uploads and processing. The API accepts various file formats, extracts text, and summarizes the content.

File Handling: Proper error handling ensures that unsupported file types and file size limits are respected. Temporary storage is used for uploaded files during processing.

# Frontend Implementation

The frontend comprises an HTML form that allows users to upload documents and trigger the summarization process. The form features:
A file input for selecting documents.
A submit button that sends the file to the Flask backend using an AJAX request.
A section to display the summary once processed.

# Backend Implementation

The backend is developed using Flask, with an API endpoint to manage file uploads. Key components include:
A route (/upload) to handle POST requests containing uploaded files.
Functions to validate file types, extract text from documents, and summarize the content.
Proper error handling for unsupported file types and exceeding file size limits.

# Usage Instructions
Uploading Documents: Open the web application in our browser. Use the file input to select a document (pdf,docx,txt,etc). Then click the "summarize" button to upload the document.
Viewing Summaries: Once the file is processed, the summary will be displayed in the designated section below the form. If there are issues with the file an error message will be shown.
Handling Unsupported File Types: The application will validate the file format before processing. Users will receive an error message if the uploaded file is not supported.
Handling Large Documents: A file size limit (e.g., 16MB) is enforced. If a user attempts to upload a file exceeding this limit, an error message will be displayed.

#  Code Overview
Document Handling in Flask: The Flask app manages file uploads and uses libraries to extract text from documents. Temporary storage is utilized to manage files during processing.
Summarization Logic: This component takes the extracted text and generates a summary, which is returned as a JSON response to the frontend.
Frontend Upload Management: JavaScript handles form submission and displays the summary dynamically without page refresh.
