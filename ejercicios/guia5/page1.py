from flask import Flask
app = Flask(__name__)  # Create the object app from Flask

@app.route("/")  # For app, we are going to route the home page
def main():      # This python function is routed to home page
    return "Hola mundo, flask"

if __name__ == "__main__": # If this file is run directly (not imported)
    app.run()              # Start the web server


