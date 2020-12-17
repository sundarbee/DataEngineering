import cassandra

### Create a connection to the database

from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)
# Create a keyspace to do the work in 
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS udacity 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)

# loansupport@hdfcbank.com
except Exception as e:
    print(e)
    
# Connect to the Keyspace
try:
    session.set_keyspace('udacity')
except Exception as e:
    print(e)
    
query = "CREATE TABLE IF NOT EXISTS Song"
query = query + "(song_title text,artist_name text,year text,album_name text,single text, PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)

query = "INSERT INTO Song (song_title,artist_name,year,album_name,single)" 
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, ("Across The Universe", "The Beatles", 1970, "False", "Let It Be"))
except Exception as e:
    print(e)
    
try:
    session.execute(query, ("The Beatles", "Think For Yourself",1965, "False", "Rubber Soul"))
except Exception as e:
    print(e)
query = 'SELECT * FROM Song'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)
    
query = "SELECT * FROM Song WHERE year=1970 AND artist_name='The Beatles'"
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)
    
session.shutdown()
cluster.shutdown()
 