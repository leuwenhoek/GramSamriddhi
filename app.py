from flask import Flask
from flask import render_template,request,redirect
from myjson import JSONDataModule

app = Flask(__name__)

json_mod = JSONDataModule()
json_mod.save_all_data()
json_mod.plot_all()

@app.route("/")
def Gram():
    return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'POST':
        village_id = request.form['village_id']
        password = request.form['password']
        if village_id.lower() == "jitwarpur" and password == "12345":
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/electricity")
def electricity():
    data = json_mod.load_electricity_data()["jitwarr_purr_village"]["electricity_data"]
    return render_template("electricity.html", data=data)

@app.route("/water")
def water():
    data = json_mod.load_water_data()["jitwarr_purr_village"]["water_supply_data"]
    return render_template("water.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)