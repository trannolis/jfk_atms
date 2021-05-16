# Air Trafic Management System

### Mission

The purpose of this technology is to create a system that allows for coordinated communication between Air traffic Controllers and pilots that allows for safe and efficient management of air traffic at JFK.

### Authors

Hriditaa Dekate, Faizan Hussain, Neh Kundalia, Nick Tran

# Instructions

To use the repository, use `git clone https://github.com/trannolis/jfk_atms.git` in the terminal to recieve the contents of the file.

Once the contents of the repository are stored onto your computer, you first need to install the relevant libraries, which is done through `pipenv install --dev`.

Afterwards, it is required to install mongodb from https://docs.mongodb.com/manual/installation/ for testing. Make sure it is running on `localhost:27017`.

Afterwards, it is suggested to run the command `make local`. This should open up a local version of the website on `localhost:5000`.

# Make Targets

### prod

Manages commits for the projects to ensure effective deployment of relevant servers.

### tests

Runs tests pertaining to the code to ensure that it compiles and formats correctly.

### dev_env

Ensures that the terminal is situated with the correct files to have the appropriate development environment for the project.

### heroku

Deploys the server to Heroku.

### docs

Ensures that the terminal starts in the correct directory to run relevant functions of the ATC.

### local

Runs the flask application on localhost:5000.

# Requirements

## Glossary

* Users refer to Air Traffic Controllers (ATCs) and pilots.
* Administrators refers to senior staff in charge of maintaining the ATC system.

### Authentication

* Administrator can register new users.
* Users can sign in to ATC.
* Users can sign out of ATC.
* Administrators can delete accounts.

### Communication

* Pilots are notified of any changes to their flight's intended gate or runway.
* Pilots and Air Traffic Controllers are able to communicate through the system.

### Database

##### Schedule

* Users can monitor schedules for air traffic.
* Users can report errors in air traffic schedule to administrators.

##### Air Traffic

* Users can find the relevant information of a particular aircraft.
* Air Traffic Controllers can change the gate that an airplane to scheduled to arrive at.
* Air Traffic Controllers can chnage the runway that an airplane is scheduled to arrive/or depart at.
* Pilots can confirm that they are on the runway or gate when they have reached said location.

# Documentation

Relevant documentation is located in [`jfk_atms/documentation`](https://github.com/trannolis/jfk_atms/tree/master/Documentation)

* [`SRS`](https://github.com/trannolis/jfk_atms/blob/master/Documentation/CS4513-SRS-003-Group-A11-1.pdf)
* [`Terminal and flight data planning`](https://github.com/trannolis/jfk_atms/blob/master/Documentation/Terminal%20Structure%20and%20Flight%20Data%20Planning.pdf)
* [`ATMS content diagram`](https://github.com/trannolis/jfk_atms/blob/master/Documentation/atms_component_diagram.png)
