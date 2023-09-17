from flask import Blueprint,render_template

views = Blueprint(__name__,"views")

#test 
@views.route("/")
def home():
    return render_template("index.html")
