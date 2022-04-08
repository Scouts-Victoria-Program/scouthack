#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
import json
from os import path

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/program')
def list_programs():
    programs = []
    try:
        with open('programs.jsonl') as f:
            for line in f:
                programs.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass
    return render_template('program.html', programs=programs)


@app.route('/program/new', methods=['POST', 'GET'])
def new_program():
    error = None
    if request.method == 'POST':
        program = {
            'author': request.form['author'], 'idea': request.form['idea']}
        with open('programs.jsonl', 'a') as f:
            json.dump(program, f)
            f.write('\n')
        return redirect(url_for('list_programs'))
    return render_template('new_program.html')


if __name__ == "__main__":
    app.run(debug=True)
