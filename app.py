from flask import Flask, request, render_template
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ForVoxySecretKey'


def count_words(text):
    text = text.strip()
    char_count = len(text)
    text = text.strip().translate(str.maketrans('', '', string.punctuation))
    word_count = len(text.split())
    return word_count, char_count


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def main_count():
    word_count, char_count = count_words(request.form['text'])
    print(word_count, char_count)
    return render_template('index.html', wordCount=word_count, charCount=char_count, text=request.form['text'])


if __name__ == '__main__':
    app.run()
