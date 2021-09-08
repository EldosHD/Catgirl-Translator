from os import remove
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        inputText = request.form["inputText"]
        if inputText != "":
            print("Translating: " + inputText)
            langParser(inputText)

        return render_template("home.html") 
    else:
        return render_template("home.html")

@app.route("/next/")
def next():
    return render_template("nextWebsite.html")
@app.route("/about/")
def about():
    return render_template("about.html")

def langParser(inputText):
    wordList = inputText.split()
    for word in wordList:
        print(word)

if __name__ == "__main__":
    app.run(debug=True,port=6969)
