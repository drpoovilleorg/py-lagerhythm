#!/usr/bin/env/python
# py-lagerhythm 0.1
# port of lagerhythm 0.2.1 (perl) to python
# https://github.com/sadsfae/py-lagerhythm

from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)
app.debug = True

import pivo

@app.route("/post_pivo", methods=["POST"])
def postpivo():
	comments = request.form['comments']
	longitude = request.form['long']
	latitude = request.form['lat']
	pivo.api.update_status(status='%s' % comments, long=longitude, lat=latitude)
	return redirect(url_for('done'))

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/post_done")
def done():
	return render_template("post_done.html")

if __name__ == '__main__':
    app.run()

