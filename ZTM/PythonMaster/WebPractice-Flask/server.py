from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def render_page(page_name):
    return render_template(f"{page_name}")

def write_to_file(data):
    with open("database.txt",mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

@app.route("/submit_form",methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("thankyou.html")
    else:
        return "Something went wrong. Try Again"