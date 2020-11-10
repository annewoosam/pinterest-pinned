from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Pin(db.Model):
    """A class for pins ."""
    
    __tablename__ = 'pins'

    pin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    board_name = db.Column(db.String)

    email_date=db.Column(db.Date)

    image_url=db.Column(db.String)

    image_name=db.Column(db.String)

    def __repr__(self):
        return f'<Pin pin_id={self.pin_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///pinterest_pins', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)