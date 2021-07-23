from flask import render_template

class Price:
    def pricePage(self):
        return render_template("price.html")