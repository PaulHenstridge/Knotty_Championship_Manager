from flask import Flask, render_template, request, redirect
from flask import Blueprint
import pdb

import repositories.team_repository as team_repository
import repositories.transfer_repository as transfer_repository
import repositories.player_repository as player_repository

from models.transfer import Transfer

transfers_blueprint = Blueprint("transfers", __name__)


@transfers_blueprint.route("/transfers")
def all_transfers():
    transfers =transfer_repository.select_all()
    
    return render_template("/transfers/transfers.html", transfers=transfers)


@transfers_blueprint.route("/transfers/new")
def new_transfer():
    all_teams = team_repository.select_all()
    all_players = player_repository.select_all()
    return render_template("/transfers/new.html", teams=all_teams, players=all_players)


@transfers_blueprint.route("/transfers/new", methods=["POST"])
def save_transfer():
 
    player = player_repository.select(request.form["player_id"])
    team_from = team_repository.select(request.form["team_from_id"])
    team_to = team_repository.select(request.form["team_to_id"])
    transfer_fee = request.form["transfer_fee"]
    status = "PENDING"

    new_transfer = Transfer(player, team_from, team_to, transfer_fee, status)

    transfer = transfer_repository.save(new_transfer)
    return render_template("/transfers/transfer.html", transfer=transfer)

# TODO -  think I need an update route to update status of the transfer.


# @transfers_blueprint.route("/transfers/play", methods=["POST"])
# def play():
#     transfer_id = request.form["transfer-id"]
#     transfer = transfer_repository.select(int(transfer_id))
#     transfer.play()

#     transfer_repository.update(transfer)
#     team_repository.update_stats(match.team1)
#     team_repository.update_stats(match.team2)
#     return render_template("/transfers/match.html", match=match)
