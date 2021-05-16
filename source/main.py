"""
This is the main function for the ATMS
"""

from flask import render_template, request, session, url_for, redirect,\
    Blueprint
from .extensions import mongo, bcrypt
import random
from math import dist
from datetime import datetime, timedelta
main = Blueprint('main', __name__)


@main.route('/')
def hello():
    flag = mongo.db['admin'].find_one() is None
    return render_template('landing.html', flag=flag)


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
    """Creates a session for a valid user"""
    # grabs information from the forms
    username_input = request.form['username']
    password_input = request.form['password']
    role = request.form['role']
    # hash the password from the forum

    # get user's hashed password from the your_database
    user = mongo.db[role].find_one_or_404({'username': username_input})
    if(bcrypt.check_password_hash(user['password'], password_input)):
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
    """Redirects to either Pilot or ATC registration pages"""
    role = request.form['role']
    if role == 'pilot':
        return redirect(url_for('main.registerPilot'))
    return redirect(url_for('main.registerAtc'))


@main.route('/registerPilot', methods=['GET', 'POST'])
def registerPilot():
    """Renders Pilot Registration Page"""
    return render_template('registerPilot.html')


@main.route('/registerAtc', methods=['GET', 'POST'])
def registerAtc():
    """Renders ATC Registration Page"""
    return render_template('registerAtc.html')


# Authenticates the registration for new admins
@main.route('/registerAdminAuth', methods=['GET', 'POST'])
def registerAdminAuth():
    """Adds checks for existing Admin user and adds new Admin
                                          User to Database"""

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

    mongo.db.admin.insert_one({
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
    """Adds checks for existing Admin user and adds new ATC
                                          User to Database"""

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

    mongo.db.atc.insert_one({
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
    """Adds checks for existing Admin user and adds new Pilot
                                          User to Database"""
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
    airportList = ['ORD', 'SFO', 'JAX', 'HCM', 'CHA', 'DFW']

    mongo.db.pilot.insert_one({
        'username': username,
        'password': hashed,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'phone_no': phone_no,
        'airplaneID': newAirplaneID})

    # make a flight to correspond with the pilot too - FAKE DATA GENERATION

    td = timedelta(0.69420)

    mongo.db.flight.insert_one({
        '_id': newAirplaneID,
        'arrivalTime': datetime.now(),
        'departureTime': datetime.now() + td,
        'departureLocation': random.choice(airportList),
        'arrivalLocation': 'JFK',
        'airplaneID': newAirplaneID,
        'gate': -1,
        'runway': -1})
    calculateGate(newAirplaneID)
    return render_template('adminHome.html')


@main.route('/adminHome')
def adminHome():
    """Renders Admin User's Home page"""
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
        flight = mongo.db['flight'].find_one_or_404({'airplaneID':
                                                     int(airplaneID)})
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
        return render_template('atc_landing.html', firstName=firstName,
                               flights=flights)
    except Exception:
        return render_template('atc_landing.html', firstName=firstName)


@main.route('/showUser', methods=['GET', 'POST'])
def showUser():
    """This method renders the show users page"""
    return render_template('showUser.html')


@main.route('/selectUser', methods=['GET', 'POST'])
def selectUser():
    """This method gets all ATCs, Admins, and Pilots"""
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
    """This methid removes the user from the either atc, admin, or atc
                                                           database"""
    role = session.get('role', None)  # gets role of the person being deleted
    delete_user = request.form.get('user')  # user to be deleted
    mongo.db[str(role)].delete_one({"username": str(delete_user)})
    return render_template('successfulDeletion.html', user=delete_user)


@main.route('/getFlights', methods=['GET', 'POST'])
def getFlights():
    '''This method fetches and displays all flights from the database'''
    flights = [flight for flight in mongo.db['flight'].find()]
    return render_template('show_flights.html', flights=flights)


@main.route('/showFlights', methods=["GET", "POST"])
def showFlights():
    """This method gets all flights from the database"""

    flight_id = request.form.get("select")
    session['select'] = flight_id
    update = request.form.get("update")
    if update == 'gate':
        return redirect('/vacantGates')
    elif update == 'runway':
        return redirect('/vacantRunways')


@main.route('/occupiedGates', methods=["GET", "POST"])
def occupiedGates():
    """ATC can change gate number"""
    availableGates = mongo.db['gate'].find({'is_vacant': {'$eq': False}})
    gates_arr = [gate for gate in availableGates]
    return render_template('occupiedGates.html', gates=gates_arr)


@main.route('/occupiedRunways', methods=["GET", "POST"])
def occupiedRunways():
    """ATC can change runway number"""
    availableRunways = mongo.db['runway'].find({'is_vacant': {'$eq': False}})
    runways_arr = [gate for gate in availableRunways]
    new_runwayID = request.form.get("select")
    session['new_runwayID'] = new_runwayID
    return render_template('occupiedRunways.html', runways=runways_arr)


@main.route('/vacateGate', methods=["GET", "POST"])
def vacateGate():
    """ATC can change Gate number for a flight"""
    toVacate = request.form.get("select")
    mongo.db['flight'].update_one({'gate': int(toVacate)}, {'$set':
                                  {'gate': -1}})
    mongo.db['gate'].update_one({'_id': int(toVacate)}, {'$set':
                                {'is_vacant': True}})
    next_flight = mongo.db['queue']\
        .find_one_and_delete({'waiting_for': 'gate'})
    if next_flight:
        mongo.db['flight'].update_one({'_id': int(next_flight['_id'])},
                                      {'$set': {'gate': toVacate}})
    return redirect('/getFlights')


@main.route('/vacateRunway', methods=["GET", "POST"])
def vacateRunway():
    """ATC can change Runway number for a flight"""
    toVacate = request.form.get("select")
    mongo.db['flight'].update_one({'runway': int(toVacate)}, {'$set':
                                  {'runway': -1}})
    mongo.db['runway'].update_one({'_id': int(toVacate)}, {'$set':
                                  {'is_vacant': True}})
    next_flight = mongo.db['queue']\
        .find_one_and_delete({'waiting_for': 'runway'})
    if next_flight:
        mongo.db['flight'].update_one({'_id': int(next_flight['_id'])},
                                      {'$set': {'runway': toVacate}})
        return redirect('/getFlights')


@main.route('/vacantGates', methods=["GET", "POST"])
def vacantGates():
    """ATC can change gate number"""
    availableGates = mongo.db['gate'].find({'is_vacant': {'$eq': True}})
    gates_arr = [gate for gate in availableGates]
    return render_template('vacantGates.html', gates=gates_arr)


@main.route('/vacantRunways', methods=["GET", "POST"])
def vacantRunways():
    """ATC can change runway number"""
    availableRunways = mongo.db['runway'].find({'is_vacant': {'$eq': True}})
    if not availableRunways:
        error = "No runways available currently"
        return render_template('vacantRunways.html', error=error)
    runways_arr = [gate for gate in availableRunways]
    new_runwayID = request.form.get("select")
    session['new_runwayID'] = new_runwayID
    return render_template('vacantRunways.html', runways=runways_arr)


@main.route('/changeGate', methods=["GET", "POST"])
def changeGate():
    """ATC can change Gate number for a flight"""
    new_gateID = request.form.get("select")
    flight_id = session.get('select')
    old_flight = mongo.db['flight'].find_one({'_id': int(flight_id)})
    old_gate = old_flight['gate']
    mongo.db['flight'].update_one({'_id': int(flight_id)}, {'$set':
                                  {'gate': int(new_gateID)}})
    mongo.db['gate'].update_one({'_id': int(new_gateID)}, {'$set':
                                {'is_vacant': False}})
    mongo.db['gate'].update_one({'_id': int(old_gate)}, {'$set':
                                {'is_vacant': True}})
    return redirect('/getFlights')


@main.route('/changeRunway', methods=["GET", "POST"])
def changeRunway():
    """ATC can change Runway number for a flight"""
    runwayID = request.form.get("select")
    flight_id = session.get('select')
    old_flight = mongo.db['flight'].find_one({'_id': int(flight_id)})
    old_runway = old_flight['runway']
    mongo.db['flight'].update_one({'_id': int(flight_id)}, {'$set':
                                  {'runway': int(runwayID)}})
    mongo.db['runway'].update_one({'_id': int(runwayID)}, {'$set':
                                  {'is_vacant': False}})
    mongo.db['runway'].update_one({'_id': int(old_runway)}, {'$set':
                                  {'is_vacant': True}})
    return redirect('/getFlights')


@main.route('/logout')
def logout():
    """This method redirects to the landing page"""
    session.pop('username')
    return redirect('/')


def calculateGate(flightId):
    """This method calculates distance from gate to runway"""
    runway = mongo.db['runway'].find_one({'is_vacant': True})
    if not runway:
        mongo.db['queue'].insert_one({'_id': flightId,
                                      'waiting_for': 'runway'})
    else:
        runway = runway['_id'], runway['x_coord'], runway['y_coord']
        gates = [(gate['_id'], gate['x_coord'], gate['y_coord']) for gate in
                 mongo.db['gate'].find({'is_vacant': True})]
        if not len(gates):
            mongo.db['queue'].insert({'_id': flightId,
                                     'waiting_for': 'gate'})
        else:
            gates = [(gate[0],
                     dist((gate[1], gate[2]),
                     (runway[1], runway[2])))
                     for gate in gates]
            gates.sort(key=lambda dist: dist[1])
            mongo.db['runway'].update({'_id': runway[0]},
                                      {'$set': {'is_vacant': False}})
            mongo.db['gate'].update({'_id': gates[0][0]},
                                    {'$set': {'is_vacant': False}})


@main.route('/chatroom', methods=['GET', 'POST'])
def chatroom():
    return render_template('chatroom.html')
