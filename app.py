class Air_Traffic_Controller:
  """" This class represents the person who will be handling the flight schedule management and assignment """
  def __init___(name, PhoneNumber, Email, Password, Airport):
    self.name = name
    self.phoneNumber = PhoneNumber
    self.email = Email
    self.password = Password #this needs to be hidden
    self.airport = Airport

  def getflights-api(self):
    """For the air traffic controller to be able to see all the flights"""
    return ...
  def requestFlightUpdate(self, flightid):
    """To see the current flight status of a particular flight"""
    return ...
  def authorizeLanding(self, flightid,location):
    """To authorize landing on the runway for a particular flight"""
    return ...
  def authorizeTakeOff(self, flightid,location):
    """To authorize takeoff on the runway for a particular flight"""
    return ...

class Pilot:
  """This class represents the pilots who will be communicating with the Air Traffic Controller"""
  def __init___(Name, PhoneNumber, Email, Password, CanLand, CanTakeOff):
    self.Name = Name
    self.PhoneNumber = PhoneNumber
    self.Email = Email
    self.Password = Password
    self.canLand = False
    self.CanTakeOff = False

  def updateFlightInfo(flightid,location,time):
    """For the pilot to be able to make any changes mid-flight if necessary"""
    return ...
  def land(self, flightId):
    """for the pilot to indicate that the plane has landed"""
    return ...
  def takeOff(self, flightid):
    """for the pilot to indicate that the plane has taken off"""
    return ...

class Flight:
  """This class represents the flights that might be landing, taxiing or taking off"""
  def __init___(flightID, airplaneID, arrivalTime, departureTime,                   arrivalLocation, departureLocation, Location):
    # Note: need to address location in air vs location on ground
    self.flightId = flightID
    self.airplaneID = airplaneID
    self.arrivalTime = arrivalTime
    self.departureTime = departureTime
    self.arrivalLocation = arrivalLocation
    self.departureLocation = departureLocation
    self.Location= Location

  def getArrivalTime(self):
    """to be able to see arrival time of the flight"""
    return arrivalTime

  def getDepartureTime(self):
    """to be able to see depature time of the flight"""
    return departureTime

  def __del__(self):
    """No cancel function"""
    return ...

  def setArrivalTime(self, time):
    """Setters for arrival and depature times and locations"""
    self.arrivalTime = time
    return True

  def setDepartureTime(self, time):
    self.departureTime = time
    return True

  def changeArrivalLocation(self,location):
    self.arrivalLocation = location
    return True

  def changeDepatureLocation(self,location):
    self.departureLocation = location
    return True


class Location:
  """This represents the individual gates at the airport"""
  def __init___(AiportCode, Gate, IsVacant):
    self.AirportCode = AiportCode
    self.Gate = Gate
    self.IsVacant = False

  def updateVacancyStatus(self, vacancyStatus):
    """to change the status gate availability"""
    self.vacancyStatus = vacancyStatus

  def getVacancyStatus(self):
    """to get current status of the gates of the arrival gate"""
    return self.IsVacant

class Airport:
  """This represents the airport at which the planes will be landing and taking off"""
  def __init___(flights, AirTrafficControllers, runway1=False,                      runway2=False, runway3=False, runway4=False):
    self.flights = flights
    self.AirTrafficControllers = AirTrafficControllers

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
