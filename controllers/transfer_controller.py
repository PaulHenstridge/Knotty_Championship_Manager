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
    teams = team_repository.select_all()
    players = player_repository.select_all()
    return render_template("/transfers/new.html", teams=teams, players=players)


@transfers_blueprint.route("/transfers/new", methods=["POST"])
def save_transfer():

    player = player_repository.select(request.form["player"])
    print("team ids in save in controller ", player.team_id, request.form["team_to"])
    team_from = team_repository.select(player.team_id) 
    team_to = team_repository.select(request.form["team_to"])
    print("IDs of team from, to at instantiation ", team_from.id, team_to.id)
    transfer_fee = request.form["transfer_fee"]

    new_transfer = Transfer(player, team_from, team_to, transfer_fee)
    transfer = transfer_repository.save(new_transfer)
    print( transfer.team_to.name)
    return render_template("/transfers/transfer.html", transfer=transfer)

# TODO - 

    def update_transfer(transfer):
        # an admin route?
        pass


@transfers_blueprint.route("/transfer/<id>/accept")
def accept_transfer(id):
    print("Accepted!")
    transfer = transfer_repository.select(id)
    transfer.confirm()
    transfer_repository.update(transfer)
    player_repository.update(transfer.player)
    team_repository.update(transfer.team_from)
    team_repository.update(transfer.team_to)

    return render_template("/transfers/transfer.html", transfer=transfer)


@transfers_blueprint.route("/transfer/<id>/negotiate")
def negotiate_transfer(id):
    transfer = transfer_repository.select(id)
    transfer.nogotiate()
    transfer_repository.update(transfer)
    return render_template("/transfers/transfer.html", transfer=transfer)

@transfers_blueprint.route("/transfer/<id>/decline")
def decline_transfer(id):
    transfer = transfer_repository.select(id)
    transfer.decline()
    transfer_repository.update(transfer)
    return render_template("/transfers/transfer.html", transfer=transfer)




# @transfers_blueprint.route("/transfers/play", methods=["POST"])
# def play():
#     transfer_id = request.form["transfer-id"]
#     transfer = transfer_repository.select(int(transfer_id))
#     transfer.play()

#     transfer_repository.update(transfer)
#     team_repository.update_stats(match.team1)
#     team_repository.update_stats(match.team2)
#     return render_template("/transfers/match.html", match=match)
