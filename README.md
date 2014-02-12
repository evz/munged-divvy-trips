# Munged Divvy

What you have here is:

1. A python script (``make_geojson.py``) that I used to generate the
``stations.geojson`` file. 

2. A python script (``clean_data.py``) that I used to clean up the raw trips
data into something that I could insert into PostgreSQL,

3. A requirements file that tells you the python modules you need to make the
python scripts run.

4. A SQL file to make the trip table in PostgreSQL without any data in it.

5. A SQL file that has a PostGIS dump of the stations table.

6. A GZipped SQL file that has a PostgreSQL dump of the trip table.

7. A GZipped CSV file with the raw trip data in it.

8. A GZipped CSV file that has the cleaned up trip data in it.

9. A CSV file containing a distance matrix between all stations (from @tothebeat)

10. A CSV file containing a first stab at joining the trips table to the
distance matrix

SQL query for trips to distance join:

``` sql
    SELECT trip.trip_id, 
        trip.starttime, 
        trip.stoptime, 
        trip.bikeid, 
        trip.tripduration, 
        trip.from_station_id, 
        trip.from_station_name, 
        trip.to_station_id, 
        trip.to_station_name, 
        trip.usertype, 
        trip.gender, 
        trip.birthyear, 
        distance.station_start, 
        distance.station_end, 
        distance.distance_meters 
    FROM trip 
    JOIN distance ON from_station_id = station_start 
        AND to_station_id = station_end 
    ORDER BY distance.distance_meters DESC;
```
