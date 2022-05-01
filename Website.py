#!/usr/bin/python3
from flask import Flask, render_template, request
from Translator import translate
from sys import platform

app = Flask(__name__)

data = {} #init dictionary

if platform == "linux" or platform == "linux2":
    # linux
    dic =open("./dictionary.txt").readlines()
elif platform == "darwin":
    # mac os
    print("This does not run on macOS")
    exit()
elif platform == "win32":
    # Windows...
    dic =open("Catgirl-Translator\dictionary.txt").readlines()

for line in dic:
    trans = line.split(" -> ")                      #read line and separate normal and furry
    data[trans[0]] = trans[1].replace("\n", "")     #save translation into dictionary

#----------Website Start ----------
@app.route("/", methods=["POST","GET"])
def home():
    translation = ""
    if request.method == "POST":
        inputText = request.form["inputText"]
        if inputText != "":
            print("Translating: " + inputText)
            translation = translate(inputText, data)
            print("Translation: " + translation)

        return render_template("home.html", inputArea=inputText, outputArea=translation) 
    else:
        return render_template("home.html")

@app.route("/dictionary/")
def dictionary():
    return render_template("dictionary.html", data=data)

@app.route("/about/")
def about():
    return render_template("about.html")
#----------Website End-----------



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
