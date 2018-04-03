from flask import render_template

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
