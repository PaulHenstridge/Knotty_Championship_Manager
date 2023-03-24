from flask import Flask, render_template

# importt controllers
app = Flask(__name__)

# register blueprints


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
