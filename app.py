from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

# load all the chapters
chpt = [] 
with open('chapters.json') as f:
    chpt = json.load(f)
print(chpt)

@app.route('/')
def index():
    return render_template('index.html', title="Vim master guide", bar="vmg")

@app.route('/c')
def chapters():
    return render_template('chapters.html', title="Chapters", bar="vmg/chapters", chapters=chpt)

@app.route('/license')
def license():
    return render_template('license.html', title="License", bar="vmg/license")

@app.route('/c/<cid>')
def chapter(cid:int):
    if int(cid) < len(chpt) + 1:
        # it was a valid chapter id
        t = ""
        for c in chpt:
            if c[1] == int(cid):
                # set the title of the page as the title of the chapter
                t = c[0]
                return render_template(f'chapters/{cid}.html', title=t, bar=f"vgm/chapters/{cid}")
    return redirect(url_for('e404'))

@app.route('/e/404')
@app.errorhandler(404)
def e404(err=None):
    return '<h1>404</h1>', 404

if __name__ == '__main__':
    app.run(debug=True)
