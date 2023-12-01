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
    
    teams = []
    for id in team_ids:
        team = team_repository.select(id)
        teams.append(team)
    tournament = Tournament(teams)
    tournament_repository.save(tournament)    
    
    return render_template("/tournaments/tournament.html", tournament=tournament)
