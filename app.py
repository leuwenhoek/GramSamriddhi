from flask import Flask
from flask import render_template,request,redirect

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)