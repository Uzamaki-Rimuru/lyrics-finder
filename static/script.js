async function askAI(type) {
    const topic = document.getElementById('topic').value;
    const output = document.getElementById('output');
    const loading = document.getElementById('loading');

    if (!topic) return alert("Please enter a topic!");

    loading.style.display = "block";
    output.innerText = "";

    // This sends a request to your Python Flask server
    const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: type, topic: topic })
    });

    const data = await response.json();
    loading.style.display = "none";
    output.innerText = data.result;
}

function clearOutput() {
    // This clears the text box
    document.getElementById('topic').value = "";
    // This clears the AI's response
    document.getElementById('output').innerText = "";
    document.getElementById('song-info').style.display = "none"
}

function copyToClipboard() {
    const outputText = document.getElementById('output').innerText;

    if (!outputText) {
        alert("Nothing to copy yet!");
        return;
    }

    navigator.clipboard.writeText(outputText).then(() => {
        alert("Lyrics copied to clipboard! 📋");
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}

function downloadLyrics() {
    const text = document.getElementById('output').innerText;
    const topic = document.getElementById('topic').value || "lyrics";

    if (!text) return alert("Nothing to download!");

    const element = document.createElement('a');
    const file = new Blob([text], { type: 'text/plain' });
    element.href = URL.createObjectURL(file);
    element.download = `${topic}.txt`;
    document.body.appendChild(element); // Required for Firefox
    element.click();
}

function askAI(type) {
    const topic = document.getElementById('topic').value;
    const loader = document.getElementById('loader');
    const output = document.getElementById('output');

    if (!topic) {
        alert("Please enter a song name first!");
        return;
    }

    // 1. Show the loader and clear old results
    loader.style.display = "block";
    output.innerText = "";

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: topic })
    })
        .then(response => response.json())
        .then(data => {
            // 2. Hide the loader when data arrives
            loader.style.display = "none";
            output.innerText = data.result;
        })
        .catch(error => {
            loader.style.display = "none";
            output.innerText = "Error connecting to server.";
            console.error('Error:', error);
        });
}

// Inside your .then(data => { ... }) block:

loader.style.display = "none";
if (data.image) {
    document.getElementById('song-info').style.display = "block";
    document.getElementById('album-cover').src = data.image;
    document.getElementById('song-display-title').innerText = data.title + " - " + data.artist;
    output.innerText = data.result;
} else {
    output.innerText = data.result;
}

function askAI(type) {
    const topic = document.getElementById('topic').value;
    const loader = document.getElementById('loader');
    const output = document.getElementById('output');

    // Determine which Python route to call
    let targetRoute = (type === 'mood') ? '/mood' : '/generate';

    loader.style.display = "block";

    fetch(targetRoute, {  // Use the targetRoute variable here
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ topic: topic })
    })
    // ... rest of your fetch code stays the same
}