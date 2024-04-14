from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['target_language']

    translator = Translator()
    translation = translator.translate(text, dest=target_language)

    translated_text = translation.text

    return render_template('result.html', original_text=text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)