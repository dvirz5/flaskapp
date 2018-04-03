from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from contextlib import closing

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'sql11225792'
app.config['MYSQL_DATABASE_PASSWORD'] = 'lhAAJB5wUu'
app.config['MYSQL_DATABASE_DB'] = 'sql11225792'
app.config['MYSQL_DATABASE_HOST'] = 'sql11.freemysqlhosting.net'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/showSignin')
def showSignUp():
    return render_template('signup.html')


@app.route('/showSignUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        
        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call the MySQL
            
            with closing(mysql.connect()) as conn:
                print ('ook')
                with closing(conn.cursor()) as cursor:
                    _hashed_password = generate_password_hash(_password)
                    cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
                    data = cursor.fetchall()
                   
                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'message':'User created successfully !'})
                    else:
                        return json.dumps({'error':str(data[0])})
            
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
            print ('ook')
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == '__main__':
    app.run(port=5002)
