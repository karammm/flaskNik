from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/public/")
def FUN_public():
    return render_template("public_page.html")

def print_hi(name):
    pass
if __name__ == "__main__":
    app.run(debug=True, host="localhost")
