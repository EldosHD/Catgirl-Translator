from os import remove
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        inputText = request.form["inputText"]
        if inputText != None:
            print("Do sth")

        return render_template("home.html") 
    else:
        return render_template("home.html")

@app.route("/next/")
def next():
    return render_template("nextWebsite.html")



if __name__ == "__main__":
    app.run(debug=True,port=6543)
