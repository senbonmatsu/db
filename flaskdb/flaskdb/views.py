"""
A Sample Web-DB Application for DB-DESIGN lecture
Copyright (C) 2022 Yasuhiro Hayashi
"""
from flask import Blueprint, request, session, render_template, redirect, flash, url_for
import datetime
import pickle

from flaskdb import apps, db, da
from flaskdb.models import User, Item,Task
from flaskdb.forms import LoginForm, AddItemForm, SearchItemForm,AddTaskForm,SearchCategoryForm

app = Blueprint("app", __name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("/index.html")

@app.route("/now", methods=["GET", "POST"])
def now():
    return str(datetime.datetime.now())

# This is a very danger method
@app.route("/receive", methods=["GET", "POST"])
def receive():
    if request.method == "GET":
        username = request.args.get("username")
        password = request.args.get("password")
    else:
        username = request.form["username"]
        password = request.form["password"]

    return render_template("receive.html", username=username, password=password)

@app.route("/initdb", methods=["GET", "POST"])
def initdb():
    db.drop_all()
    db.create_all()#db作成
    
    admin = User(username="admin", password="password")
    user = User(username="user", password="password")
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    return "initidb() method was executed. "

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)

        user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if user is None or user.password != form.password.data:
            flash("Username or Password is incorrect.", "danger")
            return redirect(url_for("app.login"))

        session["username"] = user.username
        return redirect(url_for("app.index"))

    return render_template("login.html", form=form)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("username", None)
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("app.index"))

@app.route("/additem", methods=["GET", "POST"])
def additem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        db.session.add(item)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = Item.query.all()
    return render_template("additem.html", form=form, itemlist=itemlist)

@app.route("/addtask", methods=["GET", "POST"])
def addtask():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddTaskForm()

    if form.validate_on_submit():
        task = Task()
        form.copy_to(task)
        #user = User.query.filter_by(username=session["username"]).first()
        db.session.add(task)
        db.session.commit()

        flash("An item was added.", "info")
        return redirect(url_for("app.addtask"))

    tasklist = Task.query.all()
    return render_template("addtask.html", form=form, tasklist=tasklist)#formでクラスを作成

@app.route("/searchitem", methods=["GET", "POST"])
def searchitem():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = SearchItemForm()

    if form.validate_on_submit():
        itemlist = Item.query.filter(Item.itemname.like("%" + form.itemname.data + "%")).all()        
        return render_template("search.html", form=form, itemlist=itemlist)

        # For change to PRG
        # itemlist = pickle.dumps(itemlist)
        # session["itemlist"] = itemlist
        # return redirect(url_for("app.searchitem"))

    # if "itemlist" in session:
    #     itemlist = session["itemlist"]
    #     itemlist = pickle.loads(itemlist)
    #     session.pop("itemlist", None)
    # else:
    #     itemlist = None
    # 
    # return render_template("search.html", form=form, itemlist=itemlist)

    return render_template("search.html", form=form)

@app.route("/search_category", methods=["GET", "POST"])#編集途中
def search_category():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = SearchCategoryForm()

    if form.validate_on_submit():
        itemlist = Task.query.filter(Task.category.like("%" + form.category.data + "%")).all()        
        return render_template("search_category.html", form=form, itemlist=itemlist)

    return render_template("search_category.html", form=form)

@app.route("/nativesql", methods=["GET", "POST"])
def nativesql():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddItemForm()

    if form.validate_on_submit():
        item = Item()
        form.copy_to(item)
        user = User.query.filter_by(username=session["username"]).first()
        item.user_id = user.id
        da.add_item(item)

        flash("An item was added.", "info")
        return redirect(url_for("app.additem"))

    itemlist = da.search_items()
    return render_template("additem.html", form=form, itemlist=itemlist)

@app.route("/nativesql2", methods=["GET", "POST"])
def nativesql2():
    if not "username" in session:
        flash("Log in is required.", "danger")
        return redirect(url_for("app.login"))

    form = AddTaskForm()

    if form.validate_on_submit():
        item = Task()
        form.copy_to(item)
        #user = User.query.filter_by(username=session["username"]).first()
        #item.user_id = user.id
        da.add_item(item)

        flash("An item was added.", "info")
        return redirect(url_for("app.addtask"))

    tasklist = da.search_items()
    return render_template("addtask.html", form=form, tasklist=tasklist)
