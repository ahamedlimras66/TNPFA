from flask import Blueprint
from model.price import Price

price = Blueprint("price", __name__)

priceObj = Price()

price.add_url_rule("/", view_func=priceObj.pricePage, methods=['GET'])