from flask import Flask, render_template
import dbFunctions
import time

app = Flask(__name__)

@app.route("/")
def main():
    sensorEvents = dbFunctions.getAllEvents()
    for event in sensorEvents:
        event["dateHum"] = time.strftime(" %Z - %Y/ %m/ %d, %H: %M: %S", time.localtime(event["date"]))

    return render_template('index4.html', sensorEvents=sensorEvents)

@app.route("/sensor/<sensorID>")
def sensor(sensorID):
    sensorEvents = dbFunctions.getAllEventsFrom(sensorID)
    for event in sensorEvents:
        event["dateHum"] = time.strftime("%Z - %Y/%m/%d, %H:%M:%S", time.localtime(event["date"]))

    return render_template('index4.html', sensorEvents=sensorEvents)

if __name__ == "__main__":
    app.run()