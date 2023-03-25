from flask import Flask, render_template, request
from flask import Blueprint

import repositories.team_repository as team_repository

from models.team import Team

teams_blueprint = Blueprint("teams", __name__)


# show all teams
@teams_blueprint.route("/teams")
def all_teams():
    teams = team_repository.select_all()
    return render_template("/teams/teams.html", teams=teams)


# show add a new team form
@teams_blueprint.route("/teams/new")
def new_team():
    return render_template("teams/new.html")


# add new team


@teams_blueprint.route("/teams/new", methods=["POST"])
def add_team():
    name = request.form["team-name"]
    attack = request.form["att"]
    defence = request.form["def"]
    # create new team obj
    team = Team(name, attack, defence, 0, 0)
    team_repository.save(team)
    return render_template("/teams/team.html", team=team)


# show a team by id
@teams_blueprint.route("/teams/<id>")
def team_by_id(id):
    team = team_repository.select(id)
    return render_template("/teams/team.html", team=team)
