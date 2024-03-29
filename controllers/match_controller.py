from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository

from models.player import Player

matches_blueprint = Blueprint("matches", __name__)


@matches_blueprint.route("/matches")
def all_matches():
    matches = match_repository.select_all()
    return render_template("/matches/matches.html", matches=matches)


@matches_blueprint.route("/matches/new")
def new_match():
    all_teams = team_repository.select_all()
    return render_template("/matches/new.html", all_teams=all_teams)


@matches_blueprint.route("/matches/new", methods=["POST"])
def save_match():
    match = match_repository.save(request.form["team1"], request.form["team2"])
    return render_template("/matches/match.html", match=match)


@matches_blueprint.route("/matches/play", methods=["POST"])
def play():
    match_id = request.form["match-id"]
    match = match_repository.select(int(match_id))
    goal_scorers = match.play()
    match_repository.update(match)
    team_repository.update_stats(match.team1)
    team_repository.update_stats(match.team2)

    for player in goal_scorers:
         if isinstance(player, Player):
            player.goals +=1
            player_repository.update(player)

    return render_template("/matches/match.html", match=match)
