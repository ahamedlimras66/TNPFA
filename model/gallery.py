from flask import render_template

class Gallery:
    def galleryPage(self):
        return render_template("gallery.html")