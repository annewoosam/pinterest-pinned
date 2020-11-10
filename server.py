"""Server for YourFolder app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Pin, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_pins():

    stats=crud.get_pins()
    
    pin_id=[q[0] for q in db.session.query(Pin.pin_id).all()]

    channel_name=[q[0] for q in db.session.query(Pin.channel_name).all()]
     
    board_name=[q[0] for q in db.session.query(Pin.board_name).all()]

    email_date=[q[0] for q in db.session.query(Pin.email_date).all()]

    image_url=[q[0] for q in db.session.query(Pin.image_url).all()]
      
    image_name=[q[0] for q in db.session.query(Pin.image_name).all()]

    return render_template('pins.html', pin_id=pin_id, channel_name=channel_name, board_name=board_name, email_date=email_date, image_url=image_url, image_name=image_name)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()