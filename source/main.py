"""
This is the main function for the ATMS
asdasd
asd
as
das
ads
ads
ads
dsa
dsa
das
"""

from flask import render_template, request, session, url_for, redirect,\
    Blueprint
from .extensions import mongo, bcrypt
main = Blueprint('main', __name__)


# Define a route to hello function
@main.route('/')
def hello():
    return render_template('landing.html')


# Define route for login
@main.route('/login')
def login():
    return render_template('login.html')


# Define route for register
@main.route('/register')
def register():
    return render_template('register.html')


# Authenticates the login
@main.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username_input = request.form['username']
    password_input = request.form['password']
    # hash the password from the forum

    # get user's hashed password from the your_database
    user = mongo.db.atc.find_one_or_404({'username': username_input})
    print(user['password'], password_input)
    error = None
    if(not error):
        # creates a session for the the user
        # session is a built in
        session['username'] = username_input
        return redirect(url_for('main.home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)


# Authenticates the register
@main.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    hashed = bcrypt.generate_password_hash(password)

    if mongo.db.admin.find_one({'username': username}):
        error = "This user already exists"
        return render_template('register.html', error=error)

    mongo.db.admin.insert({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no})
    return render_template('landing.html')


@main.route('/home')
def home():
    user = session['username']
    data = [1, 2, 3, 4, 5]
    return render_template('home.html', username=user, posts=data)


@main.route('/post', methods=['GET', 'POST'])
def post():
    #  username = session['username']
    #  cursor = conn.cursor();
    #  blog = request.form['blog']
    #  query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
    #  cursor.execute(query, (blog, username))
    #  conn.commit()
    #  cursor.close()
    return redirect(url_for('home'))


@main.route('/select_blogger')
def select_blogger():
    # check that user is logged in
    # username = session['username']
    # should throw exception if username not found

    #  cursor = conn.cursor();
    #  query = 'SELECT DISTINCT username FROM blog'
    #  cursor.execute(query)
    #  data = cursor.fetchall()
    #  cursor.close()
    data = [1, 2, 3, 4, 5]
    return render_template('select_blogger.html', user_list=data)


@main.route('/show_posts', methods=["GET", "POST"])
def show_posts():
    poster = request.args['poster']
    #  cursor = conn.cursor();
    #  query = 'SELECT ts, blog_post FROM blog WHERE username = %s
    #  ORDER BY ts DESC'
    #  cursor.execute(query, poster)
    #  data = cursor.fetchall()
    #  cursor.close()
    data = [1, 2, 3, 4, 5]
    return render_template('show_posts.html', poster_name=poster, posts=data)


@main.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


if __name__ == "__main__":
    pass
