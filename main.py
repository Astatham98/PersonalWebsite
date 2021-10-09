from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projects")
def page2():
    return render_template("page2.html")


if __name__ == "__main__":
    app.run(debug=True)
