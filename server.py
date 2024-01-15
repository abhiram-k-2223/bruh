from flask import Flask, request, jsonify
from summarizer import summarize_text
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    summary = summarize_text(text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
