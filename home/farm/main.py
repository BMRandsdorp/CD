# Import what we need from flask
from flask import Flask, render_template

# Create a Flask app inside `app`
app = Flask(__name__)


@app.route('/')
def index():
    # multiple lines of text for home page
    index_lines = [
        'Hello, world!',
        'This is version 4 of our home page',
        'You can find a secret page by adding /cow to the URL'
    ]

    return render_template('index.html', lines_of_text=index_lines)


@app.route('/cow')
def cow():
    return render_template('moo.html')


if __name__ == '__main__':
    app.run(debug=True)
