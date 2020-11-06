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
    return url_for('error404')


@app.route('/error/400')
@app.errorhandler(400)
def error400(err=None):
	e = {
	    'number':'400',
	    'description':'The request that this page has received is not valid. Perhaps your browser has been confused or you are using the wrong method to access this page.'
	}
	return render_template('error.html', title='400', bar="vgm/400", error=e), 400

@app.route('/error/401')
@app.errorhandler(401)
def error401(err=None):
	e = {
	    'number':'401',
	    'description':'We are sorry but you do not have authorization to access this page.'
	}
	return render_template('error.html', title='401', bar="vmg/401", error=e), 401

@app.route('/error/404')
@app.errorhandler(404)
def error404(err=None):
	e = {
	    'number':'404',
	    'description':'We could not find the page you are looking for, perhaps you have misspelled the link or the page is private.'
	}
	return render_template('error.html', title='404', bar="vmg/404", error=e), 404

@app.route('/error/500')
@app.errorhandler(500)
def error500(err=None):
	e = {
	    'number':'500',
	    'description':'Do not worry, this error is not your fault. There has been an internal error on our server. We are trying to fix it.'
	}
	return render_template('error.html', title='500', bar="vmg/500", error=e), 500

if __name__ == '__main__':
    app.run(debug=True)
