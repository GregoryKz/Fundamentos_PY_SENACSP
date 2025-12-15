from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem-vindo á minha aplicção Flask!"

@app.route("/Sobre")
def sobre():
    return "Essa é a pagina sobre."

if __name__ == "__main__":
    app.run(debug=True)