from flask import Blueprint
from model.event import Event

event = Blueprint("event", __name__)

eventObj = Event()

event.add_url_rule("/", view_func=eventObj.eventPage, methods=['GET'])