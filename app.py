from flask import Flask, render_template, url_for, redirect
import json
import os

app = Flask(__name__)

# load all the chapters
chpt = [] 
with open('data/chapters.json') as f:
    chpt = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', title="Vim master guide", bar="vimmasterguide")

@app.route('/c')
def chapters():
    return render_template('chapters.html', title="Chapters", bar="c", chapters=chpt, d="The chapter index for the VMG book!")

@app.route('/license')
def license():
    return render_template('license.html', title="License", bar="license", d="Read the license of the VMG book!")

@app.route('/u')
def rperson():
    return redirect(url_for('index'))

@app.route('/u/<name>')
def person(name:str):
    persons = os.listdir('templates/u')
    if name in [n[:-5] for n in persons]:
        return render_template(f'people/{name}.html', title=name, bar=f'u/{name}')
    return redirect(url_for('error404')) 

@app.route('/c/<cid>')
def chapter(cid:int):
    if int(cid) < len(chpt) + 1:
        # it was a valid chapter id
        t = ""
        for i, c in enumerate(chpt):
            if c[1] == int(cid):
                if i + 1 < len(chpt):
                    next_chapter = chpt[i + 1]
                else:
                    next_chapter = chpt[i]
                # set the title of the page as the title of the chapter
                t = c[0]
                return render_template(f'c/{cid}.html', title=t, bar=f"c/{cid}", post=c, next_chapter=next_chapter, d=t)
    return redirect(url_for('error404'))


@app.route('/e')
def error():
    # redirect to the index.html
    return redirect(url_for('index'))

@app.route('/e/400')
@app.errorhandler(400)
def error400(err=None):
	e = {
	    'number':'400',
	    'description':'The request that this page has received is not valid. Perhaps your browser has been confused or you are using the wrong method to access this page.'
	}
	return render_template('error.html', title='400', bar="e/400", error=e), 400

@app.route('/e/401')
@app.errorhandler(401)
def error401(err=None):
	e = {
	    'number':'401',
	    'description':'We are sorry but you do not have authorization to access this page.'
	}
	return render_template('error.html', title='401', bar="e/401", error=e), 401

@app.route('/e/403')
@app.errorhandler(403)
def error403(err=None):
	e = {
	    'number':'403',
	    'description':'The access to the requested resource is forbidden for some reason, the server understood your request but could not respond to it.'
	}
	return render_template('error.html', title='401', bar="e/401", error=e), 401
@app.route('/e/404')
@app.errorhandler(404)
def error404(err=None):
	e = {
	    'number':'404',
	    'description':'We could not find the page you are looking for, perhaps you have misspelled the link or the page is private.'
	}
	return render_template('error.html', title='404', bar="e/404", error=e), 404

@app.route('/e/500')
@app.errorhandler(500)
def error500(err=None):
	e = {
	    'number':'500',
	    'description':'Do not worry, this error is not your fault. There has been an internal error on our server. We are trying to fix it.'
	}
	return render_template('error.html', title='500', bar="e/500", error=e), 500

if __name__ == '__main__':
    app.run(debug=True)
