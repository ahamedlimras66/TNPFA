from flask import Blueprint
from model.gallery import Gallery

gallery = Blueprint("gallery", __name__)

galleryObj = Gallery()

gallery.add_url_rule("/", view_func=galleryObj.galleryPage, methods=['GET'])