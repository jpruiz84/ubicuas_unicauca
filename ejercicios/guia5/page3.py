from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    dataPage = {}
    dataPage["title"] = "Web page 2"
    dataPage["users"] = []

    user = {'nombre' : 'Julio', 'apellidos': 'Rodriguez','edad' : 19}
    dataPage["users"].append(user)

    user = {'nombre' : 'Roberto', 'apellidos': 'Contreras','edad' : 20}
    dataPage["users"].append(user)

    user = {'nombre' : 'Mario', 'apellidos': 'Marquez','edad' : 21}
    dataPage["users"].append(user)

    return render_template('index3.html',dataPage=dataPage)

if __name__ == "__main__":
    app.run()