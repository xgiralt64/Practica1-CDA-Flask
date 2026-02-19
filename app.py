from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    grup = []

    if request.method == "POST":
        noms = request.form.get("noms")

        if noms:
            grup = [nom.strip() for nom in noms.split(",")]

    return render_template("index.html", grup=grup)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
