import sqlite3
import globals

# Class to open and manage the data base from file
class opendb(object):

    def __init__(self):
        self.connection = sqlite3.connect('sensors.db3')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close

# To create a table on the DB
def createTable():

    sql = opendb()
    cursor = sql.cursor

    cursor.execute('''CREATE TABLE IF NOT EXISTS sensors (date real, address text, rssi integer,
        locationX real, locationY real, gatewayID text)''')

    sql.close()
    return True

# To insert a sensor event data in the DB
def insertSensorEvent(sensor):
    sql = opendb()

    sql.cursor.execute("INSERT INTO sensors VALUES (?,?,?,?,?,?)",
                  [sensor["date"],
                   sensor["address"],
                   sensor["rssi"],
                   globals.LOCATION_X,
                   globals.LOCATION_Y,
                   globals.GATEWAY_ID])

    sql.connection.commit()
    sql.close()
    return True

# To convert database reading into dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# To get all events from datatabase into a dictionary list
def getAllEvents():
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute("SELECT * FROM sensors")

    return cur.fetchall()

# To get all event from specified sensors into a dictonary list
def getAllEventsFrom(sensorID):
    sql = opendb()
    con = sql.connection

    con.row_factory = dict_factory
    cur = con.cursor()

    t = (sensorID,)
    cur.execute("SELECT * FROM sensors WHERE sensorID = ?", t)

    return cur.fetchall()