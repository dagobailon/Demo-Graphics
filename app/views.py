# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def DemoGraphics():
	return render_template('DemoGraphics.html')

@app.route('/DemoGraphics_2')
def DemoGraphics_2():
	return render_template('DemoGraphics_2.html')

@app.route('/DemoGraphics_3')
def DemoGraphics_3():
	return render_template('DemoGraphics_3.html')

@app.route('/survey')
def survey():
	return render_template('survey.html')

@app.route('/member')
def member():
	return render_template('member.html')