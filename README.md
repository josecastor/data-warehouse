# Data Modeling in AWS with Redshift



## **Overview**
For this project, Data Modeling in AWS with Redshift and an ETL pipeline using Python was applied. The startup Sparkify wants to analyze the data they are collecting about music and user activity in its new music streaming app. We are currently collecting data in S3 Bucket and the json format and the analytics team is particularly interested in understanding what songs users are listening to.



## **Datasets**

**Song**
Sample Record :
```
{"num_songs": 1, "artist_id": "AR8IEZO1187B99055E", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Marc Shaiman", "song_id": "SOINLJW12A8C13314C", "title": "City Slickers", "duration": 149.86404, "year": 2008}
```

**Log**
Sample Record :
```
{"artist": "Sydney Youngblood", "auth": "Logged In", "firstName": "Jacob", "gender": "M", "itemInSession": 53, "lastName": "Klein", "length": 238.07955, "level": "paid", "location": "Tampa-St. Petersburg-Clearwater, FL", "method": "PUT", "page": "NextSong", "registration": 1.540558e+12, "sessionId": 954, "song": "Ain't No Sunshine", "status": 200, "ts": 1543449657796, "userAgent": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"", "userId": "73"}
```



## **Schema**

### Staging Tables

**staging_events** - events staging of table
```
artist, auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userAgent, userId
```

**staging_songs** - song staging of table
```
song_id, num_songs, title, artist_name, artist_latitude, year, duration, artist_id, artist_longitude, artist_location
```

### Dimension Tables

**songs**  - songs of table
```
song_id, title, artist_id, year, duration
```

**artists**  - artists of table
```
artist_id, name, location, latitude, longitude
```

**time**  - time of table
```
start_time, hour, day, week, month, year, weekday
```

**users**  - users of table
```
user_id, first_name, last_name, gender, level
```

### Fact Table 

**songplays** - songplays of table
```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

## Data resume

**staging_events** - 8056 records

**staging_songs** - 14896 records

**songs** - 14896 records

**artists** - 10025 records

**time** - 8023 records

**users** - 105 records

**songplays** - 326 records


## Project Files

```create_redshift.py``` -> Code for create environment in AWS.

```create_tables.py``` -> Code for **fact** and **dimension tables** for the start schema in Redshift.

```dwh.cfg``` -> File for put your config of environment.

```etl.py``` -> load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.

```README.MD``` -> Description about process for this ETL pipeline. 

```remove_redshift.py``` -> Code for remove environment in AWS.

```sql_queries.py``` -> Code sql queries for dropping, creating and insertion tables.


## How to run

Please, place your AWS **region**, **key** and **secret** in SECTION **AWS** into ```dwh.cfg```

Run the files ```create_redshift.py```, ```create_tables.py```, ```etl.py``` and ```remove_redshift.py``` as below.

```
!python create_redshift.py
```

```
!python create_tables.py 
``` 

```
!python etl.py 
```

```
!python remove_redshift.py
```