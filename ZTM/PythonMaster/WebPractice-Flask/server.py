from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def render_page(page_name):
    print(f"{page_name}.html")
    return render_template(f"{page_name}")

@app.route("/submit_form",methods=["POST","GET"])
def submit_form():
    return "Form submitted Hoooraaaay!"