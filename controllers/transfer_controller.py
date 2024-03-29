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
    team_from = team_repository.select(player.team_id) 
    team_to = team_repository.select(request.form["team_to"])
    transfer_fee = request.form["transfer_fee"]

    new_transfer = Transfer(player, team_from, team_to, transfer_fee)
    transfer = transfer_repository.save(new_transfer)
    return render_template("/transfers/transfer.html", transfer=transfer)

# TODO - 

    def update_transfer(transfer):
        # an admin route?
        pass

# show a transfer by id
@transfers_blueprint.route("/transfers/<id>")
def transfer_by_id(id):
    transfer = transfer_repository.select(id)

    return render_template("/transfers/transfer.html", transfer=transfer)


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

