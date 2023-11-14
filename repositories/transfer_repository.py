from db.run_sql import run_sql

from models.team import Team
from models.transfer import Transfer

import repositories.team_repository as team_repository
import repositories.player_repository as player_repository


# create a new transfer
def save(transfer): # player, team_from, team_to, transfer_fee
    player_id = transfer.player.id
    team_from_id = transfer.team_from.id
    team_to_id = transfer.team_to.id
    transfer_fee = transfer.transfer_fee
    status = "PENDING"

    sql = """
    INSERT INTO transfers (player_id, team_from_id, team_to_id, transfer_fee, status) 
    VALUES (%s,%s,%s,%s,%s)
    RETURNING id
    """
    values = [player_id, team_from_id, team_to_id, transfer_fee, status]

    result = run_sql(sql, values)
    transfer.id = result[0]["id"]
    return transfer


# view all transfers
def select_all():
    transfers = []

    sql = "SELECT * FROM transfers"
    results = run_sql(sql)

    for result in results:
        player_id = player_repository.select(result["player_id"])
        team_from_id = team_repository.select(result["team_from_id"])
        team_to_id = team_repository.select(result["team_to_id"])
        transfer_fee = result["transfer_fee"]
        status = result["status"]
        id = result["id"]

        transfer = Transfer(player_id, team_from_id, team_to_id, transfer_fee, status, id)
        transfers.append(transfer)

    return transfers


# view transfers by team id
def select_by_team(id):
    transfers = []
    sql = "SELECT * FROM transfers WHERE team_from_id = %s OR team_to_id = %s"
    values = [id, id]
    results = run_sql(sql, values)

    for result in results:
        player_id = player_repository.select(result["player_id"])
        team_from_id = team_repository.select(result["team_from_id"])
        team_to_id = team_repository.select(result["team_to_id"])
        transfer_fee = result["transfer_fee"]
        status = result["status"]
        id = result["id"]
        
        transfer = Transfer(player_id, team_from_id, team_to_id, transfer_fee, status, id)
        transfers.append(transfer)

    return transfers



# view an individual transfer
def select(id):
    sql = "SELECT * FROM transfers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]

        player_id = player_repository.select(result["player_id"])
        team_from_id = team_repository.select(result["team_from_id"])
        team_to_id = team_repository.select(result["team_to_id"])
        transfer_fee = result["transfer_fee"]
        status = result["status"]
        id = result["id"]
        
        transfer = Transfer(player_id, team_from_id, team_to_id, transfer_fee, status, id)

    return transfer


# update a transfer after the decision is known
def update(transfer):
    sql = """UPDATE transfers SET (status) = (%s)
    WHERE id = %s"""
    values = [transfer.status, transfer.id]
    run_sql(sql, values)


# delete all transfers
def delete_all():
    sql = "DELETE FROM transfers"
    run_sql(sql)
