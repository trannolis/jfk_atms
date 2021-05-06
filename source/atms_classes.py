class Air_Traffic_Controller:
    """" This class represents the person who will be handling the flight
    schedule management and assignment """
    def __init___(self, name, phoneNumber, email, password, airport):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password  # this needs to be hidden
        self.airport = airport

    def getflights_api(self):
        """For the air traffic controller to be able to see all the flights"""
        return ...

    def requestFlightUpdate(self, flightid):
        """To see the current flight status of a particular flight"""
        return ...

    def authorizeLanding(self, flightid, location):
        """To authorize landing on the runway for a particular flight"""
        return ...

    def authorizeTakeOff(self, flightid, location):
        """To authorize takeoff on the runway for a particular flight"""
        return ...


class Pilot:
    """This class represents the pilots who will be communicating with the
    Air Traffic Controller"""
    def __init___(self, name, phoneNumber, email, password, canLand,
                  canTakeOff):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password
        self.canLand = False
        self.canTakeOff = False

    def updateFlightInfo(flightid, location, time):
        """For the pilot to be able to make any changes mid-flight if
        necessary"""
        return ...

    def land(self, flightId):
        """for the pilot to indicate that the plane has landed"""
        return ...

    def takeOff(self, flightid):
        """for the pilot to indicate that the plane has taken off"""
        return ...


class Flight:
    """This class represents the flights that might be landing, taxiing or
    taking off"""
    def __init___(self, flightID, airplaneID, arrivalTime, departureTime,
                  arrivalLocation, departureLocation, location):
        # Note: need to address location in air vs location on ground
        self.flightId = flightID
        self.airplaneID = airplaneID
        self.arrivalTime = arrivalTime
        self.departureTime = departureTime
        self.arrivalLocation = arrivalLocation
        self.departureLocation = departureLocation
        self.location = location

    def getArrivalTime(self, arrivalTime):
        """to be able to see arrival time of the flight"""
        return arrivalTime

    def getDepartureTime(self, departureTime):
        """to be able to see depature time of the flight"""
        return departureTime

    def __del__(self):
        """No cancel function"""
        return ...

    def setArrivalTime(self, time):
        """Setter for arrival time"""
        self.arrivalTime = time
        return True

    def setDepartureTime(self, time):
        """Setter for departure time"""
        self.departureTime = time
        return True

    def changeArrivalLocation(self, location):
        """Setter for arrival location"""
        self.arrivalLocation = location
        return True

    def changeDepatureLocation(self, location):
        """Setter for departure location"""
        self.departureLocation = location
        return True


class Location:
    """This represents the individual gates at the airport"""
    def __init___(self, aiportCode, gate, isVacant):
        self.airportCode = aiportCode
        self.gate = gate
        self.isVacant = False

    def updateVacancyStatus(self, vacancyStatus):
        """to change the status gate availability"""
        self.vacancyStatus = vacancyStatus

    def getVacancyStatus(self):
        """to get current status of the gates of the arrival gate"""
        return self.isVacant


class Airport:
    """This represents the airport at which the planes will be
    landing and taking off"""
    def __init___(self, flights, airTrafficControllers, runway1=False,
                  runway2=False, runway3=False, runway4=False):
        self.flights = flights
        self.airTrafficControllers = airTrafficControllers

    def addFlight(self, flightid):
        """to add new flight record at the airport"""
        return True

    def updateRunway1(self, new_status):
        """updates status of runway1"""
        self.runway1 = new_status
        return True

    def updateRunway2(self, new_status):
        """updates status of runway2"""
        self.runway2 = new_status
        return True

    def updateRunway3(self, new_status):
        """updates status of runway3"""
        self.runway3 = new_status
        return True

    def updateRunway4(self, new_status):
        """updates status of runway4"""
        self.runway4 = new_status
        return True
