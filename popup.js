document.addEventListener('DOMContentLoaded', function () {
    const inputPage = document.getElementById('inputPage');
    const outputPage = document.getElementById('outputPage');
    const textInput = document.getElementById('textInput');
    const summarizedText = document.getElementById('summarizedText');
    const summarizeButton = document.getElementById('summarizeButton');

    function sendRequest(url, method, body) {
        return fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
        })
        .then(response => {
            console.log('Response status:', response.status);
            return response.json();
        })
        .catch(error => console.error('Error:', error));
    }

    summarizeButton.addEventListener('click', function () {
        const inputText = textInput.value;
        const serverURL = 'http://localhost:5000/summarize';
        sendRequest(serverURL, 'POST', { text: inputText })
            .then(data => {
                console.log('Received data:', data);

                if (data && data.summary) {
                    const summary = data.summary;

                    summarizedText.textContent = summary;

                    inputPage.style.display = 'none';
                    outputPage.style.display = 'block';
                } else {
                    console.error('Invalid response format');
                }
            });
    });
});
