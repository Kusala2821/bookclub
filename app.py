from flask import Flask, render_template, request, session, redirect, make_response,url_for
from flask_session import Session
from datetime import timedelta
import time
import config
import datetime
from user import User
import pymysql



app = Flask(__name__,static_url_path='')
app.config.from_object(config)


app.config['SECRET_KEY'] = 'IA637project'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
sess = Session()
sess.init_app(app)

@app.route('/')  #route name
def home(): #view function
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        u = User()
        if u.register_user(username=username, password=password, confirm_password=confirm_password):
            return redirect(url_for('login'))
        else:
            return render_template('register.html', title='Register', errors=u.errors)

    return render_template('register.html', title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.form.get('username') is not None and request.form.get('password') is not None:
            u = User()
            if u.tryLogin(request.form.get('username'), request.form.get('password')):
                #if len(u.data) > 0:
                    print("Login successful")
                    session['user'] = u.data[0]['username']
                    session['active'] = time.time()
                    return render_template('main.html', title='eBook Store - Main')
            else:
                print("Login failed: Incorrect username or password")
                return render_template('login.html', title='Sign In', msg='Incorrect username or password.')
        else:
            if 'msg' not in session.keys() or session['msg'] is None:
               m = 'Type your email and password to continue.'
            else:
               m = session['msg']
               session['msg'] = None
            return render_template('login.html', title='Sign In', msg=m)

if __name__ == '__main__':
    app.run(debug=True)



