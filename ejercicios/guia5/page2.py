from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    dataPage = {}
    dataPage["title"] = "Web page 2"
    dataPage["nombre"] = "Marcos"
    dataPage["apellidos"] = "Torres"
    dataPage["edad"] = 30

    return render_template('index2.html',dataPage=dataPage)

if __name__ == "__main__":
    app.run()