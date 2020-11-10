"""CRUD operations."""

from model import db, Pin, connect_to_db

import datetime


def create_pin(channel_name, board_name, email_date, image_url, image_name):
   

    pin = Pin(channel_name=channel_name,
                  board_name=board_name,
                  email_date=email_date,
                  image_url=image_url,
                  image_name=image_name)

    db.session.add(pin)

    db.session.commit()

    return pin

def get_pins():
    """Return all rows of pin data."""

    return Pin.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
