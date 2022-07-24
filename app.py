from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    title = "Signos LTDA"
    return render_template("index.html", title=title)

@app.route("/signo_chines")
def chines():
    title = "Signo Chinês"
    return render_template("signo_chines.html",title=title)

if __name__ == "__main__":
    app.run(debug=True)


