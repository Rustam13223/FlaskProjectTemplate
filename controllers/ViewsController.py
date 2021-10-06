from flask import render_template
from app import mongo


def home():
    return render_template("home.html")
