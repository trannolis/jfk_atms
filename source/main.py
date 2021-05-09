"""
This is the main function for the ATMS
"""

from flask import render_template, request, session, url_for, redirect,\
    Blueprint
from .extensions import mongo, bcrypt
import random
from datetime import datetime
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
    """This method returns the pilot's flight information to the pilot landing
    page"""
    username = session['username']  # gets pilot's username
    pilot = mongo.db['pilot'].find_one_or_404({'username': username})
    first_name = pilot['firstName']
    airplaneID = pilot['airplaneID']
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


@main.route('/showUser', methods=['GET', 'POST'])
def showUser():
    return render_template('showUser.html')


@main.route('/selectUser', methods=['GET', 'POST'])
def selectUser():
    role = request.form.get("role")
    session['role'] = role
    if role == 'atc':
        atcs = mongo.db['atc'].find({}, {'_id': 0, 'username': 1})
        atcs_arr = [x for x in atcs]
        return render_template('deleteATC.html', user_list=atcs_arr, role=role)
    elif role == 'pilot':
        pilots = mongo.db['pilot'].find({}, {'_id': 0, 'username': 1})
        pilot_arr = [x for x in pilots]
        return render_template('deletePilot.html', user_list=pilot_arr,
                               role=role)
    else:
        admins = mongo.db['admin'].find({}, {'_id': 0, 'username': 1})
        admins_arr = [x for x in admins]
        return render_template('deleteAdmin.html', user_list=admins_arr,
                               role=role)


@main.route('/removeUser', methods=['GET', 'POST'])
def removeUser():
    """removes the user from the either atc, admin, or atc database"""
    role = session.get('role', None)  # gets role of the person being deleted
    delete_user = request.form.get('user')  # user to be deleted
    print(delete_user)
    mongo.db[str(role)].remove({"username": str(delete_user)})
    print("success")
    return render_template('successfulDeletion.html', user=delete_user)


@main.route('/getFlights', methods=['GET', 'POST'])
def getFlights():
    '''This method fetches and displays all flights from the database'''
    flights = [flight for flight in mongo.db['flight'].find()]
    calculateGate(1)
    return render_template('show_flights.html', flights=flights)


@main.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


def calculateGate(flightId):
    runway = mongo.db['runway'].find_one({'is_vacant': True})
    gates = [(gate['_id'], gate['x_coord'], gate['y_coord']) for gate in
             mongo.db['gate'].find({'is_vacant': True})]
    print(runway, gates)

# @main.route('/chatroom', methods=['GET', 'POST'])
# def sessions():
#     return render_template('chatroom.html')


# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')


# @socketio.on('my event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my event: ' + str(json))
#     socketio.emit('my response', json, callback=messageReceived)
