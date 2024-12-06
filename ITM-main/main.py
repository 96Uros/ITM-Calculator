from flask import Flask, render_template, request, make_response


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    itm = None
    if request.method == "POST":
        try:
            visina = float(request.form.get("visina"))
            teza = float(request.form.get("teza"))
            itm = teza / (visina/100) ** 2
            manjsi_itm = round(itm, 2)
            response = make_response(render_template("rezultat.html", itm=itm, manjsi_itm=manjsi_itm))
            response.set_cookie("itm", str(manjsi_itm))
            return response
        except (ValueError, TypeError):
            itm = "Vnesi veljavno številko!"
    return render_template("index.html")

@app.route("/rezultat")
def rezultat():
    itm = request.cookies.get("itm")
    return render_template("rezultat.html", itm=itm)

if __name__ == "__main__":
    app.run(use_reloader=True)

