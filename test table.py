from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask,request

from flask import render_template

app = Flask(__name__)

VerifyAccountStatus = True


@app.route('/coin/<name>')
def hello(name=None):
    return render_template('coin.html', name=name)
 



if __name__ == "__main__":
    app.run()
