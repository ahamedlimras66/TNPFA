from flask import Flask, url_for
from route.home import home
from route.about import about
from route.event import event
from route.gallery import gallery
from route.price import price

app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(about, url_prefix="/about")
app.register_blueprint(event, url_prefix="/event")
app.register_blueprint(gallery, url_prefix="/gallery")
app.register_blueprint(price, url_prefix="/price")


if __name__ == "__main__":
    app.run(debug=True)