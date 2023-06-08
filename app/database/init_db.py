from db import get_db_connection

conn = get_db_connection()

cur = conn.connection.cursor()


cur.execute("DROP TABLE IF EXISTS stations;")
cur.execute(
    "CREATE TABLE stations (id serial PRIMARY KEY,"
    "station_id varchar (20) NOT NULL UNIQUE,"
    "name varchar (150) NOT NULL,"
    "address varchar (150) NOT NULL,"
    "is_returning boolean DEFAULT '0',"
    "is_renting boolean DEFAULT '0',"
    "is_installed boolean DEFAULT '0',"
    "num_docks_available int,"
    "num_bikes_available int,"
    "last_reported date,"
    "latitude numeric NOT NULL,"
    "longitude numeric NOT NULL);"
)

cur.execute("CREATE INDEX idx_stations_station_id ON stations(station_id);")


conn.connection.commit()

cur.close()
conn.connection.close()
