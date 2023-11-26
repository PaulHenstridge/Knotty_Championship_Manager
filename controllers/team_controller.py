from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository

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
    team_type = request.form["team-type"]
    team = Team(name, 0, 0, 0, 0)

    team_id = team_repository.save(team)
    team.team_id = team_id

    new_players = team.generate_players(team_type)
    team_repository.update(team)

    for player in new_players:
        player_repository.save(player)
    return render_template("/teams/team.html", team=team, players=new_players)


# show a team by id
@teams_blueprint.route("/teams/<id>")
def team_by_id(id):
    team = team_repository.select(id)
    players = player_repository.select_all_by_team_id(id)    
    return render_template("/teams/team.html", team=team, players=players)

# show edit team form
@teams_blueprint.route("/teams/<id>/edit")
def edit(id):
    team = team_repository.select(id)
    return render_template("/teams/edit.html", team=team)


@teams_blueprint.route("/teams/edit", methods=["POST"])
def edit_team():
    name = request.form["name"]
    attack = request.form["attack"]
    defence = request.form["defence"]
    matches_played = request.form["matches_played"]
    wins = request.form["wins"]
    id = request.form["id"]

    team = Team(name, attack, defence, matches_played, wins, id)
    team_repository.update(team)
    return render_template("/teams/team.html", team=team)


@teams_blueprint.route("/teams/<id>/matches")
def matches_by_team(id):
    matches = match_repository.select_by_team((id))
    return render_template("/matches/matches.html", matches=matches)


@teams_blueprint.route("/teams/<id>/delete")
def delete(id):
    team_repository.delete(id)
    return redirect("/teams")
