from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login = True, index = True)

@app.route("/batches")
def batches():
    return render_template("batches.html", login = True,  batch = True)
@app.route("/attendence")
def attendence():
    return render_template("attendence.html", login = True, attendence = True)

@app.route("/login")
def login():
    return render_template("login.html", login = True,  login1 = True)

@app.route("/register")
def register():
    return render_template("register.html" , login = True,  register = True)

@app.route("/inventors")
def inventors():
    inventorsData = [{"id": "1111", "name": "Vidit Gupta", "address": "MHV 20/401", "mobile": "9958495900", "startDate": "123456", "email": "gupta.vidit@icloud.com"}, 
                   {"id": "2222", "name": "Shyla Gupta", "address": "MHV 20/401", "mobile": "9958495900", "startDate": "123456", "email": "gupta.shyla@icloud.com"}]
    return render_template("inventors.html", login = True, inventorsData = inventorsData, inventors = True)    

