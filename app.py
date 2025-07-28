from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Language mapping (EN to other languages)
language_models = {
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "it": "Helsinki-NLP/opus-mt-en-it",
    "en": "Helsinki-NLP/opus-mt-ROMANCE-en"
}

@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_text = ""
    selected_language = "fr"
    if request.method == 'POST':
        input_text = request.form['text']
        selected_language = request.form['language']
        model_name = language_models.get(selected_language)
        translator = pipeline("translation", model=model_name)
        translated_text = translator(input_text)[0]['translation_text']
    return render_template("index.html", translated_text=translated_text, selected_language=selected_language)

if __name__ == '__main__':
    app.run(debug=True)