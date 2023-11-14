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

# TODO -  think I need an update route to update status of the transfer.
    # will be called when a transfer is clicked accepted / decliner
    #  or  when re-negotiating - update fee, change status to "NEGOTIATING" ( update enum)
    # or   in the edit route?  not really realistic to edit details of an offer so prob not

    # interaction calls controller -> uses id to get details from DB, instantiates a Transfer instance
    # calls method on class instance... eg accept, decline, negotiate
    # methods update the instances values.  
    # instance passed to the repository.update() method to be added to DB
    # and passed to a template to show the new status of the transfer.

    # so what routes?  do all in update, or have transfers/accept ,transfers/decline etc?

    def update_transfer(transfer):
        pass

    # UPDATE: player team and team_id, both temas bank_balance, transfer_status
    # not here though - seperate method i think.   this is for creatig new.
    # above would happen on accept or decline - update route!

# @transfers_blueprint.route("/transfers/play", methods=["POST"])
# def play():
#     transfer_id = request.form["transfer-id"]
#     transfer = transfer_repository.select(int(transfer_id))
#     transfer.play()

#     transfer_repository.update(transfer)
#     team_repository.update_stats(match.team1)
#     team_repository.update_stats(match.team2)
#     return render_template("/transfers/match.html", match=match)
