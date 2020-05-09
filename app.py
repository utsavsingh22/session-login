from flask import Flask,request,render_template,session
import os

app = Flask(__name__,template_folder='template')

app.secret_key = os.urandom(24)

@app.route('/')
def hello_world():
    return render_template("login.html")
database={'utsav singh':'password','DUA':'123','GOYAL':'123'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    password=request.form['password']
    if name1 not in database:
	    return render_template('login.html',info='Invalid User')
    else:
        if database[name1]!=passwords:
            return render_template('login.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return render_template('login.html')             

if __name__ == '__main__':
    app.run(debug=True)