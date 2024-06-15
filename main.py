from flask import Flask, render_template, request
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main.html', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter(style='colorful')
        highlighted_code = highlight(code, lexer, formatter)
        return render_template('main.html', code=highlighted_code, prev_code=code)
    return render_template('main.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
