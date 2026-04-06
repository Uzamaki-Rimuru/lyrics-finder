from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the AI model (we use distilgpt2 for speed on local machines)
print("Loading AI Brain... this may take a minute.")
ai_generator = pipeline('text-generation', model='distilgpt2')


@app.route('/')
def home():
    # This serves your HTML file
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    task_type = data.get('type')
    topic = data.get('topic')

    if task_type == 'lyrics':
        prompt = f"Write 90s Grunge lyrics about {topic}:\nVerse 1:"
    else:
        prompt = f"A formal debate on {topic}.\nPerson A: I argue that"

    # AI generates the response
    result = ai_generator(prompt, max_length=150, temperature=0.8)
    ai_text = result[0]['generated_text']

    return jsonify({"result": ai_text})


if __name__ == "__main__":
    app.run(debug=True)
