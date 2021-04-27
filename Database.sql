CREATE TABLE ATC (
        username VARCHAR(32),
        password VARCHAR(64),
        firstName VARCHAR(32),
        lastName VARCHAR(32),
        email VARCHAR(32),
        phoneNumber VARCHAR(10),
        airportCode VARCHAR(5),
        PRIMARY KEY (username)
);

CREATE TABLE Pilot (
        username VARCHAR(32),
        password VARCHAR(64),
        firstName VARCHAR(32),
        lastName VARCHAR(32),
        email VARCHAR(32),
        phoneNumber VARCHAR(10),
        airplaneId VARCHAR(10),
        landStatus INT,
        takeoffStatus INT,
        PRIMARY KEY (username)
);

CREATE TABLE Airport (
		airportName VARCHAR(10),
        PRIMARY KEY (airportName)

);

CREATE TABLE Airplane (
	airplaneID VARCHAR(10),
    PRIMARY KEY (airplaneID)
);

CREATE TABLE Flight (
        arrivalTime TIMESTAMP,
        departureTime TIMESTAMP,
        latitude DECIMAL(9,6),
        longitude DECIMAL(8,6),
        flightId VARCHAR(10),
        arrivalLocation VARCHAR(10),
        departureLocation VARCHAR(10),
        airplaneId VARCHAR(10),
        PRIMARY KEY (flightId),
        FOREIGN KEY (arrivalLocation) REFERENCES Airport (airportName),
        FOREIGN KEY (departureLocation) REFERENCES Airport (airportName),
        FOREIGN KEY (airplaneId) REFERENCES Airplane (airplaneId)
);
