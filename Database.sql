CREATE TABLE ATC (
        username VARCHAR(32),
        password VARCHAR(64),
        firstName VARCHAR(32),
        lastName VARCHAR(32),
        email VARCHAR(32),
        phoneNumber VARCHAR(10),
        PRIMARY KEY (username),
        FOREIGN KEY (airportName) REFERENCES Airport (airportName)
);

CREATE TABLE Pilot (
        username VARCHAR(32),
        password VARCHAR(64),
        firstName VARCHAR(32),
        lastName VARCHAR(32),
        email VARCHAR(32),
        phoneNumber VARCHAR(10),
        landStatus INT,
        takeoffStatus INT,
        PRIMARY KEY (username)
);

CREATE TABLE Flight (
        arrivalTime DATETIMEOFFSET (-7),
        departureTime DATETIMEOFFSET (-7),
        latitude DECIMAL(9,6),
        longitude DECIMAL(8,6),
        PRIMARY KEY (flightId),
        FOREIGN KEY (arrivalLocation) REFERENCES Airport (airportName),
        FOREIGN KEY (departureLocation) REFERENCES Airport (airportName),
        FOREIGN KEY (airplaneId) REFERENCES Airplane (airplaneId)
);
