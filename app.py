from flask import Flask, url_for
from route.home import home



app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)