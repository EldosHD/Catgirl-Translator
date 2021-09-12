from flask import Flask, render_template, request
from Translator import translate

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    translation = ""
    if request.method == "POST":
        inputText = request.form["inputText"]
        if inputText != "":
            print("Translating: " + inputText)
            translation = translate(inputText)
            print("Translation: " + translation)

        return render_template("home.html", inputArea=inputText, outputArea=translation) 
    else:
        return render_template("home.html")

@app.route("/dictionary/")
def dictionary():
    dic =open("C:\\Users\\Valen\\Github\\Catgirl-Translator\\dictionary.txt").readlines()
    return render_template("dictionary.html", dic=dic)

@app.route("/about/")
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=6969)
