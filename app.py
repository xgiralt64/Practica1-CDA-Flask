from flask import Flask, render_template, request
from database import init_db, guardar_grup, carregar_grup

app = Flask(__name__)

#inicialitzem la BD
init_db()

# Responem si la ruta és /
@app.route("/", methods=["GET", "POST"])
def index():
    #En cas que el tipus de petició sigui POST:
    if request.method == "POST":
        #Agafem els noms del formulari
        noms_text = request.form.get("noms")

        if noms_text:
            grup = [nom.strip() for nom in noms_text.split(",")]
            #I després de separar-los per "," els guardem a la BD
            guardar_grup(grup)
    #En cas que la petició no sigui post, agafem de la base de dades el grup guardat i li passem al HTML
    grup = carregar_grup()
    return render_template("index.html", grup=grup)


# App allotjada al port 8000 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
