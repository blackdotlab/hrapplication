from flask import Flask, render_template, redirect, url_for, request, session, abort, flash, render_template_string
import os
from app import app

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("index.html")        
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'hradmin' or request.form['password'] != 'C&p7H8i3&ht6b':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Successful login.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
