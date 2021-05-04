"""
This is the main function for the ATMS
"""

from flask import render_template, request, session, url_for, redirect,\
    Blueprint
from .extensions import mongo, bcrypt
main = Blueprint('main', __name__)


# Define a route to hello function
@main.route('/')
def hello():
    return render_template('landing.html')


@main.route('/login')
def login():
    return render_template('login.html')


# Define route for registering admins
@main.route('/registerAdmin')
def registerAdmin():
    return render_template('registerAdmin.html')


# Authenticates the login for users
@main.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username_input = request.form['username']
    password_input = request.form['password']
    role = request.form['role']
    # hash the password from the forum

    # get user's hashed password from the your_database
    user = mongo.db[role].find_one_or_404({'username': username_input})
    print(user['password'], password_input)
    error = None
    if(not error):
        # creates a session for the the user
        # session is a built in
        session['username'] = username_input
        return redirect(url_for('main.' + role + 'Home'))
    else:
        # returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)


@main.route('/register', methods=['GET', 'POST'])
def register():
    role = request.form['role']
    if role == 'pilot':
        return redirect(url_for('main.registerPilot'))
    return redirect(url_for('main.registerAtc'))


@main.route('/registerPilot', methods=['GET', 'POST'])
def registerPilot():
    return render_template('registerPilot.html')


@main.route('/registerAtc', methods=['GET', 'POST'])
def registerAtc():
    return render_template('registerAtc.html')


# Authenticates the registration for new admins
@main.route('/registerAdminAuth', methods=['GET', 'POST'])
def registerAdminAuth():
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
    return render_template('adminHome.html')


# Authenticates the registration for new ATCs
@main.route('/registeAtcAuth', methods=['GET', 'POST'])
def registerAtcAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    hashed = bcrypt.generate_password_hash(password)

    if mongo.db.atc.find_one({'username': username}):
        error = "This user already exists"
        return render_template('home.html', error=error)

    mongo.db.admin.insert({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no})
    return render_template('adminHome.html')


# Authenticates the registration for new pilots
@main.route('/registerPilotAuth', methods=['GET', 'POST'])
def registerPilotAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    hashed = bcrypt.generate_password_hash(password)

    if mongo.db.pilot.find_one({'username': username}):
        error = "This user already exists"
        return render_template('register.html', error=error)

    mongo.db.admin.insert({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no})
    return render_template('adminHome.html')


@main.route('/adminHome')
def adminHome():
    user = session['username']
    return render_template('adminHome.html', username=user)


@main.route('/post', methods=['GET', 'POST'])
def post():
    return redirect(url_for('home'))


@main.route('/select_blogger')
def select_blogger():
    data = [1, 2, 3, 4, 5]
    return render_template('select_blogger.html', user_list=data)


@main.route('/show_posts', methods=["GET", "POST"])
def show_posts():
    poster = request.args['poster']
    data = [1, 2, 3, 4, 5]
    return render_template('show_posts.html', poster_name=poster, posts=data)


@main.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')
