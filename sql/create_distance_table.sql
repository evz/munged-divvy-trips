DROP TABLE IF EXISTS distance;

CREATE TABLE distance(
    city VARCHAR(8),
    station_start INTEGER,
    station_end INTEGER,
    distance_meters INTEGER,
    station_start_latitude FLOAT8,
    station_start_longitude FLOAT8,
    station_end_latitude FLOAT8,
    station_end_longitude FLOAT8,
    PRIMARY KEY(station_start, station_end)
);
