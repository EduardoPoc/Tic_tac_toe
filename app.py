from flask import Flask, render_template

app = Flask(__name__)

def tabuleiro_vazio():
    return [" "] * 9

@app.route("/")
def index():
    return render_template(
        "index.html", 
        tabuleiro=tabuleiro_vazio() )


if __name__ == "__main__":
    app.run(debug=True)
