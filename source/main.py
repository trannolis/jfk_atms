from flask import Flask, render_template, request, session, url_for, redirect


from flask import Blueprint
from .extensions import mongo
from .extensions import bcrypt

salt = "Tandon"
main = Blueprint('main', __name__)

#Dependencies:
#pip install pipenv
#pipenv install flask flask_pymongo python-dotenv
#pipenv install 'mongo[srv]' dnspython python-dotenv
#pipenv install flask flask_bcrypt python-dotenv

"""
@main.route('/')
def index():
    pilot_collection = mongo.db.pilot
    pilot_collection.insert({'username': 'nick_user', 'password': '123', 'firstName': 'Nick', 'lastName' : 'Tran'})
    return '<h1> "Added Pilot" </h1>'
"""

#Define a route to hello function
@main.route('/')
def hello():
    return render_template('landing.html')

#Define route for login
@main.route('/login')
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
salt = "Tandon"

#Initialize the app from Flask
app = Flask(__name__)
bcrypt = Bcrypt(app)

#pip install flask-mongoengine
#pip install flask-bcrypt
#pip install flask_pymongo
#brew tap mongodb/brew
#brew install mongocli

#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

#Define route for login
@app.route('/login')

def login():
    return render_template('login.html')

#Define route for register

@main.route('/register')
def register():
    return render_template('register.html')

#Authenticates the login

@main.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    #grabs information from the forms
    username_input = request.form['username']
    password_input = request.form['password']
    #hash the password from the forum
    hashed = bcrypt.hashpw(password_input, salt)

    #get user's hashed password from the your_database
    user = mongo.atms.atc.find("username" : username).find_one_or_404()
    if 404():
      return render_template('login.html', error=error)
    else:
      hashed_password = bcrypt.hashpw(password_input, salt)

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM user WHERE username = %s and password = %s'
    cursor.execute(query, (username, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['username'] = username
        return redirect(url_for('home'))
    else:
        #returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)

#Authenticates the register
@main.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    hashed = bcrypt.hashpw(password, salt)

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, (username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        ins = 'INSERT INTO user VALUES(%s, %s)'
        cursor.execute(ins, (username, password))
        conn.commit()
        cursor.close()
    return render_template('index.html')


@main.route('/home')
def home():
    user = session['username']
    cursor = conn.cursor();
    query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    cursor.execute(query, (user))
    data = cursor.fetchall()
    cursor.close()
    return render_template('home.html', username=user, posts=data)


@main.route('/post', methods=['GET', 'POST'])
def post():
    username = session['username']
    cursor = conn.cursor();
    blog = request.form['blog']
    query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
    cursor.execute(query, (blog, username))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))

@main.route('/select_blogger')
def select_blogger():
    #check that user is logged in
    #username = session['username']
    #should throw exception if username not found

    cursor = conn.cursor();
    query = 'SELECT DISTINCT username FROM blog'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('select_blogger.html', user_list=data)

@main.route('/show_posts', methods=["GET", "POST"])
def show_posts():
    poster = request.args['poster']
    cursor = conn.cursor();
    query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    cursor.execute(query, poster)
    data = cursor.fetchall()
    cursor.close()
    return render_template('show_posts.html', poster_name=poster, posts=data)

@main.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

main.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
