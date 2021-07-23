from flask import render_template

class Event:
    def eventPage(self):
        return render_template("event.html")