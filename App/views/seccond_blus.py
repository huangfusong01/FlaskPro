from flask import Blueprint, render_template, request

blue = Blueprint('seccond',__name__)


@blue.route("/login/",methods=['get','post'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == 'POST':
        #  username是web传的值，丢到request里头来的
        username = request.form.get("username")

        return username