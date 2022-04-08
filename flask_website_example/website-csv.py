#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
import csv

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
    fieldnames = ['author', 'idea']
    programs = []
    try:
        with open('programs.csv') as csvfile:
            csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in csvreader:
                programs.append(row)
    except FileNotFoundError:
        pass

    return render_template('program.html', programs=programs)


@app.route('/program/new', methods=['POST', 'GET'])
def new_program():
    fieldnames = ['author', 'idea']
    if request.method == 'POST':
        program = {
            'author': request.form['author'], 'idea': request.form['idea']}
        with open('programs.csv', 'a') as csvfile:
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            csvwriter.writerow(program)

        return redirect(url_for('list_programs'))
    return render_template('new_program.html')


if __name__ == "__main__":
    app.run(debug=True)
