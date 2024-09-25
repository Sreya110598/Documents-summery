function uploadDocument() {
    const formData = new FormData(document.getElementById('uploadForm'));
    fetch('/summarize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('summary').innerText = data.summary;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
