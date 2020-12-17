import psycopg2;
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create a connection to the database
try:
    conn = psycopg2.connect("host=localhost",dbname='',user='',password='')
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
except psycopg2.Error as e:
    print('Error connecting to database')
    print(e)
    
# Use the connection to get a cursor
try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print('Could not get the cursor')
    print(e)
conn.commit()

# Creating Database
try:
    cur.execute("create database udacity_test")
except psycopg2.Error as e:
    print(e)
    
# Create table
try:
    cur.execute("CREATE TABLE IF NOT EXISTS Song (song_title VARCHAR(150),artist_name VARCHAR(50),year VARCHAR(50),album_name VARCHAR(50),single VARCHAR(50))")
except psycopg2.Error as e:
    print(e)

# Inserting Values
try:
    cur.execute("INSERT INTO Song (song_title,artist_name,year,album_name,single) VALUES (%s,%s,%s,%s,%s)", 
                    ("Across The Universe", "The Beatles", "1970", "False", "Let It Be"))
except psycopg2.Error as e:
    print(e)

# Validate Data
try:
    cur.execute("SELECT * FROM Song")
except psycopg2.Error as e:
    print(e)

# Close Connection
cur.close()
conn.close()