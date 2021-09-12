from flask import Flask, render_template, request
from Translator import translate

app = Flask(__name__)

dic =open("Catgirl-Translator/dictionary.txt").readlines()

@app.route("/", methods=["POST","GET"])
def home():
    translation = ""
    if request.method == "POST":
        inputText = request.form["inputText"]
        if inputText != "":
            print("Translating: " + inputText)
            translation = translate(inputText, dic)
            print("Translation: " + translation)

        return render_template("home.html", inputArea=inputText, outputArea=translation) 
    else:
        return render_template("home.html")

@app.route("/dictionary/")
def dictionary():
    return render_template("dictionary.html", dic=dic)

@app.route("/about/")
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=6969)
