"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb pinterest_pins')

os.system('createdb pinterest_pins')

model.connect_to_db(server.app)

model.db.create_all()


# Create Pin table's initial data.

with open('data/pin.json') as f:

    pin_data = json.loads(f.read())

pin_in_db = []

for pin in pin_data:
    channel_name, board_name, email_date, image_url, image_name= (
                                   pin['channel_name'],
                                   pin['board_name'],
                                   pin['email_date'],
                                   pin['image_url'],
                                   pin['image_name'])

    db_pin = crud.create_pin(
                                 channel_name,
                                 board_name,
                                 email_date,
                                 image_url,
                                 image_name)

    pin_in_db.append(db_pin)
