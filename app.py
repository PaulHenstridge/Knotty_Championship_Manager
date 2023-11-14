from flask import Flask, render_template, redirect, url_for
from controllers.team_controller import teams_blueprint
from controllers.match_controller import matches_blueprint
from controllers.player_controller import players_blueprint
from controllers.transfer_controller import transfers_blueprint

# import controllers
app = Flask(__name__)

# register blueprints
app.register_blueprint(teams_blueprint)
app.register_blueprint(matches_blueprint)
app.register_blueprint(players_blueprint)
app.register_blueprint(transfers_blueprint)


@app.route("/")
def main():
    return redirect(url_for('teams.all_teams'))

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
