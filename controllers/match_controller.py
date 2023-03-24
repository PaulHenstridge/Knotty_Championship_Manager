from flask import Flask, render_template, request
from flask import Blueprint

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

matches_blueprint = Blueprint("matches", __name__)


@matches_blueprint.route("/matches")
def all_matches():
    return "Matches!"


@matches_blueprint.route("/matches/new")
def new_match():
    all_teams = team_repository.select_all()
    return render_template("newmatch.html", all_teams=all_teams)


@matches_blueprint.route("/matches/new", methods=["POST"])
def save_match():
    save(request.form["team1"], request.form["team2"])
