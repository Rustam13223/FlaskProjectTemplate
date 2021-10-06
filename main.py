from flask import render_template
from app import app, mongo

from routes.views import views


app.register_blueprint(views, url_prefix='/')



if __name__ == '__main__':
    app.debug = True
    app.run()
