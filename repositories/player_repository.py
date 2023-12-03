from db.run_sql import run_sql

from models.player import Player


# add a player
def save(player):
    sql = """
    INSERT INTO players (name, position, skill_level, team_id, goals, img_url) 
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING id;
    """
    values = [player.name, player.position, player.skill_level, player.team_id, player.goals, player.img_url]
    results = run_sql(sql, values)
    player.id = results[0]["id"]


# show all players
def select_all():
    players = []
    sql = """
        SELECT players.name, players.id, players.position, players.skill_level, players.goals, players.img_url, teams.name AS team_name, teams.id AS team_id
        FROM players 
        JOIN teams ON players.team_id = teams.id
      """
    results = run_sql(sql)
    for result in results:
        player = Player(
            result["name"],
            result["position"],
            result["skill_level"],
            result["team_name"],
            result["team_id"],
            result["goals"],
            result["img_url"],
            result["id"]       
        )
        players.append(player)
    return players

 # select all by team id
def select_all_by_team_id(team_id):
    print('teamid in repository ', team_id)
    players = []
    sql = """
        SELECT players.name, players.id, players.position, players.skill_level, players.goals, players.img_url, teams.name AS team_name, teams.id AS team_id
        FROM players 
        JOIN teams ON players.team_id = teams.id
        WHERE teams.id = %s
      """
    values = [team_id]
    results = run_sql(sql,values)
    print("results in repository ", results)
    for result in results:
        player = Player(
            result["name"],
            result["position"],
            result["skill_level"],
            result["team_name"],
            result["team_id"],
            result["goals"],
            result["img_url"],
            result["id"]       
        )
        players.append(player)
    return players


# show an individual player by id
def select(id):
    player = None
    sql = """
        SELECT players.name, players.id, players.position, players.skill_level, players.goals, players.img_url, teams.name AS team_name , teams.id AS team_id
        FROM players 
        JOIN teams ON players.team_id = teams.id
        WHERE players.id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        player = Player(
            result["name"],
            result["position"],
            result["skill_level"],
            result["team_name"],
            result["team_id"],
            result["goals"],
            result["img_url"],
            result["id"]
        )
    return player


# remove a player
def delete(id):
    sql = """
    DELETE FROM players WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


# edit/update a player
def update(player):
    sql = """
    UPDATE players SET (name, position, skill_level, team_id, goals) = (%s,%s,%s,%s,%s)
    WHERE id = %s
    """
    values = [
        player.name,
        player.position,
        player.skill_level,
        player.team_id,
        player.id, 
        player.goals
       
    ]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)
