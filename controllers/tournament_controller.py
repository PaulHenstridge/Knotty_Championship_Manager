from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.tournament_repository as tournament_repository

from models.tournament import Tournament

tournaments_blueprint = Blueprint("tournaments", __name__)

@tournaments_blueprint.route("/tournaments/new")
def new_tournament():
    all_teams = team_repository.select_all()
    return render_template("/tournaments/new.html", all_teams=all_teams)


@tournaments_blueprint.route("/tournaments/new", methods=["POST"])
def save_tournament():
    team_ids = [
        request.form['team1'],
        request.form['team2'],
        request.form['team3'],
        request.form['team4'],
        request.form['team5'],
        request.form['team6'],
        request.form['team7'],
        request.form['team8']
        ]
    print("TEAM_IDS-->", team_ids)
    teams = []
    for id in team_ids:
        team = team_repository.select(int(id))
        teams.append(team)

    tournament = Tournament(teams)
    tournament = tournament_repository.save(tournament)    
    
    return render_template("/tournaments/tournament.html", tournament=tournament)

@tournaments_blueprint.route("/tournaments/play", methods=["POST"])
def play_tournament():
    tourney_id = request.form["tournament-id"]
    tournament = tournament_repository.select(int(tourney_id))

    tournament.run_tourney(tournament.teams)
    team_repository.update(tournament.winner)

    tournament_repository.update(tournament)
    # some way to add all the games played in the tourney....?
    return render_template("/tournaments/tournament.html", tournament=tournament)
