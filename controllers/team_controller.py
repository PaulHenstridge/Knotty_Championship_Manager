from flask import Flask, render_template
from flask import Blueprint

import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)


# show all teams
@teams_blueprint.route("/teams")
def all_teams():
    teams = team_repository.select_all()
    return render_template("teams.html", teams=teams)


# add a new team
@teams_blueprint.route("/teams/new")
def new_team():
    return render_template()


# show a team by id
@teams_blueprint.route("/teams/<id>")
def team_by_id(id):
    team = team_repository.select(id)
    return render_template("team.html", team=team)
