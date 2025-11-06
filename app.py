# app.py
from flask import Flask, render_template,redirect
from myjson import JSONDataModule

app = Flask(__name__)

# Initialize data module and generate all data + graphs
json_mod = JSONDataModule()
json_mod.save_all_data()
json_mod.plot_all()

@app.route("/")
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

@app.route("/projects")
def projects():
    data = json_mod.load_projects_data()["jitwarr_purr_village"]["projects"]
    projects_list = data["projects_data"]
    summary = {
        "total": data["total_projects"],
        "active": data["active_projects"],
        "completed": data["completed_projects"]
    }
    return render_template("projects.html", projects=projects_list, summary=summary)

@app.route("/complaints")
def complaints():
    return render_template("complaints.html")

@app.route("/submit-complaint", methods=["POST"])
def submit_complaint():
    # In real app: save to database, send SMS, assign ticket
    return redirect("/complaints?success=1")

if __name__ == "__main__":
    app.run(debug=True)