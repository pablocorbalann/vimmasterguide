from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', bar="vmg")

@app.route('/c')
def chapters():
    return render_template('chapters.html', title="Chapters", bar="vmg/chapters")

@app.route('/license')
def license():
    return render_template('license.html', title="License", bar="vmg/license")


if __name__ == '__main__':
    app.run(debug=True)
