from flask import Flask, render_template
from controllers.team_controller import teams_blueprint
from controllers.match_controller import matches_blueprint

# importt controllers
app = Flask(__name__)

# register blueprints
app.register_blueprint(teams_blueprint)
app.register_blueprint(matches_blueprint)


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
