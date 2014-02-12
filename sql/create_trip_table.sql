DROP TABLE IF EXISTS trip;

CREATE TABLE trip(
    trip_id INTEGER,
    starttime TIMESTAMP,
    stoptime TIMESTAMP,
    bikeid INTEGER,
    tripduration FLOAT8,
    from_station_id INTEGER,
    from_station_name VARCHAR(50),
    to_station_id INTEGER,
    to_station_name VARCHAR(50),
    usertype VARCHAR(15),
    gender VARCHAR(10),
    birthyear INTEGER,
    PRIMARY KEY(trip_id) 
);
