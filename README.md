# Air Trafiic Management System

### Mission

The purpose of this technology is to create a system that allows for coordinated communication between Air traffic Controllers and pilots that allows for safe and efficient management of air traffic at JFK.

### Authors

Hriditaa Dekate, Faizan Hussain, Neh Kundalia, Nick Tran

# Instructions

To use the repository, use `git clone https://github.com/trannolis/jfk_atms.git` in the terminal to recieve the contents of the file.

Once the contents of the repository are stored onto your computer, you first need to install the relevant libraries flask, which is done through `pip install -r $(REQ_DIR)/requirements-dev.txt`

Afterwards, it is suggested to run `python3 app.py`. When a working version of the website for jfk_atm is available, it would be suggested to navigate to `localhost:8000`

### Client

### Server

##### tests

##### prod

##### docs

###### dev_env

# Requirements

## Glossary

* Users refer to Air Traffic Controllers (ATCs) and pilots
* Administrators refers to sernior staff in charge of maintaining the ATC system

### Authentication

* Administrator can create sign up codes for new users
* Users can register for ATC with sign up code
* Users can sign in to ATC
* Users can sign out of ATC
* Administrators can delete accounts

### Communication

* Air Traffic 

### Database

##### Schedule

* Users can monitor schedules for air traffic
* Users can report errors in air traffic schedule to administrators
* Admninistrators can change the the air traffic schedule at their discretion

##### Air Traffic

* Users can find the relevant information of a particular aircraft, including
 * Aircraft Location
 * Flight Details
