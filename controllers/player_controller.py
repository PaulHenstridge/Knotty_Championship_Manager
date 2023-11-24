from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.team_repository as team_repository
import repositories.match_repository as match_repository
import repositories.player_repository as player_repository

from models.player import Player
from utils.generate_name import generate_name

players_blueprint = Blueprint("players", __name__)


# show all players
@players_blueprint.route("/players")
def all_players():
    players = player_repository.select_all()
    return render_template("/players/players.html", players=players)


# show add a new player form
@players_blueprint.route("/players/new")
def new_player():
    teams = team_repository.select_all()
    return render_template("players/new.html", teams=teams)


# add new player
@players_blueprint.route("/players/new", methods=["POST"])
def add_player():
    try:
        print("in add player ",request.form)
        name = request.form["player_name"]
        position = request.form["position"]
        skill_level = request.form["skill"]

        team_info = request.form["team"].split("|")
        team_id = team_info[0]
        team_name = team_info[1]

        # create new player obj
        _,img_url = generate_name()
        player = Player(name, position, skill_level, team_name, team_id, img_url)
        print("player to be added: ",player)
        player_repository.save(player)
        return render_template("/players/player.html", player=player)
    except Exception as e:
        print("Error: ", e)
        return str(e), 400

# show a player by id
@players_blueprint.route("/players/<id>")
def player_by_id(id):
    player = player_repository.select(id)
    return render_template("/players/player.html", player=player)

# show edit player form
@players_blueprint.route("/players/<id>/edit")
def edit(id):
    player = player_repository.select(id)
    return render_template("/players/edit.html", player=player)


@players_blueprint.route("/players/edit", methods=["POST"])
def edit_player():
    name = request.form["name"]
    position = request.form["position"]
    skill_level = request.form["skill"]
    team_id = request.form["team_id"]
    id = request.form["id"]

    # create new player obj
    player = Player(name, position, skill_level, team_id, id)
    player_repository.update(player)
    return render_template("/players/player.html", player=player)


# @teams_blueprint.route("/teams/<id>/matches")
# def matches_by_team(id):
#     matches = match_repository.select_by_team((id))
#     return render_template("/matches/matches.html", matches=matches)


@players_blueprint.route("/players/<id>/delete")
def delete(id):
    player_repository.delete(id)
    return redirect("/players")
