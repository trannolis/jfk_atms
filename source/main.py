"""
This is the main function for the ATMS
"""

from flask import render_template, request, session, url_for, redirect,\
    Blueprint
from .extensions import mongo, bcrypt
import random
from datetime import datetime
# from source import socketio
main = Blueprint('main', __name__)


# Define a route to hello function
@main.route('/')
def hello():
    return render_template('landing.html')


# Define a route to login function
@main.route('/login')
def login():
    return render_template('login.html')


# Define route for registering admins
@main.route('/registerAdmin')
def registerAdmin():
    return render_template('registerAdmin.html')


@main.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    '''Authenticates the login for users'''
    # grabs information from the forms
    username_input = request.form['username']
    password_input = request.form['password']
    role = request.form['role']

    # get user's hashed password from the your_database
    user = mongo.db[role].find_one({'username': username_input})
    if user and bcrypt.check_password_hash(user['password'],
                                           password_input):
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


@main.route('/registerAdminAuth', methods=['GET', 'POST'])
def registerAdminAuth():
    '''Authenticates the registration for new admins'''
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    hashed = bcrypt.generate_password_hash(password)

    if mongo.db.admin.find_one({'username': username}):
        error = "This user already exists"
        return render_template('registerAdmin.html', error=error)

    mongo.db.admin.insert({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no})
    return render_template('adminHome.html')


# Authenticates the registration for new ATCs
@main.route('/registerAtcAuth', methods=['GET', 'POST'])
def registerAtcAuth():
    '''Authenticates the registration for new ATCs'''
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

    mongo.db.atc.insert({
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
    '''Authenticates the registration for new ATCs'''
    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_no = request.form['phone_no']
    hashed = bcrypt.generate_password_hash(password)

    if mongo.db.pilot.find_one({'username': username}):
        error = "This user already exists"
        return render_template('registerPilot.html', error=error)

    newAirplaneID = random.randint(0, 1000)

    mongo.db.pilot.insert({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no,
        'airplaneID': newAirplaneID})

    # make a flight to correspond with the pilot too - FAKE DATA GENERATION
    mongo.db.flight.insert({
        '_id': newAirplaneID,
        'arrivalTime': datetime.now(),
        'departureTime': datetime.now(),
        'departureLocation': 'nowhere',
        'arrivalLocation': 'JFK',
        'airplaneId': newAirplaneID})

    return render_template('adminHome.html')


@main.route('/adminHome')
def adminHome():
    user = session['username']
    return render_template('adminHome.html', username=user)


@main.route('/pilotHome', methods=["GET"])
def pilotHome():
    """This method returns the pilot's flight information to the
    pilot landing page"""
    username = session['username']
    pilot = mongo.db['pilot'].find_one_or_404({'username': username})
    first_name = pilot['firstName']
    airplaneID = pilot['airplaneId']
    try:
        flight = mongo.db['flight'].find_one_or_404({'airplaneId': airplaneID})
        arrivalTime = flight['arrivalTime']
        arrivalLocation = flight['arrivalLocation']
        return render_template('pilot_landing.html', name=first_name,
                               airplaneID=airplaneID, arrivalTime=arrivalTime,
                               arrivalLocation=arrivalLocation)
    except Exception:
        return render_template('noFlight.html')


@main.route('/atcHome')
def atcHome():
    """This method returns all flights"""
    username = session['username']
    atcName = mongo.db['atc'].find_one_or_404({'username': username})
    firstName = atcName['firstName']
    try:
        flights = mongo.db['flights'].find()
        # flightIDs = flights['airplaneID']
        # arrivalTimes = flights['arrivalTimes']
        return render_template('atc_landing.html', firstName=firstName,
                               flights=flights)
    except Exception:
        return render_template('atc_landing.html', firstName=firstName)


@main.route('/getFlights', methods=['GET', 'POST'])
def getFlights():
    '''This method fetches and displays all flights from the database'''
    flights = [flight for flight in mongo.db['flight'].find()]

    return render_template('show_flights.html', flights=flights)


@main.route('/deleteUser', methods=['GET', 'POST'])
def deleteUser():
    return render_template('delete_user.html')


@main.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')

# @main.route('/chatroom', methods=['GET', 'POST'])
# def sessions():
#     return render_template('chatroom.html')


# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')


# @socketio.on('my event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my event: ' + str(json))
#     socketio.emit('my response', json, callback=messageReceived)

# for i in range(1, 139):
    #     mongo.db['gate'].insert({
    #         '_id': i,
    #         'X_coord': i*100,
    #         'y_coord': i*100,
    #         'is_vacant': bool(random.randint(0, 1)),
    #         'in_service': True,
    #         'terminal': i % 6 + 1})

    # for i in range(1, 5):
    #     mongo.db['runway'].insert({
    #         '_id': i,
    #         'x_coord': i*random.randint(100, 150),
    #         'y_coord': i*random.randint(100, 150),
    #         'is_vacant': bool(i % 2)})
