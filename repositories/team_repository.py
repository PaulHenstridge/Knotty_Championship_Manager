from db.run_sql import run_sql

from models.team import Team
from models.player import Player


# add a team to the league
def save(team):
    sql = """
    INSERT INTO teams (name, attack, defence, matches_played, wins, cup_wins, bank_balance) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    RETURNING id;
    """
    values = [team.name, team.attack, team.defence, team.matches_played, team.wins, team.cup_wins, team.bank_balance]
    results = run_sql(sql, values)
    team.id = results[0]["id"]
    return team.id


# show all teams in league
def select_all():
    teams = []
    sql = "SELECT * FROM teams ORDER BY wins DESC"
    results = run_sql(sql)
    for result in results:
        team = Team(
            result["name"],
            result["attack"],
            result["defence"],
            result["matches_played"],
            result["wins"],
            result["cup_wins"],
            result["bank_balance"],
            result["id"],
        )
        teams.append(team)
    return teams


# show an individual team by id
def select(id):
    if id != None:
        team = None
        sql = """
            SELECT * FROM teams WHERE id = %s
        """
        values = [id]
        results = run_sql(sql, values)

        if results:
            result = results[0]
            team = Team(
                result["name"],
                result["attack"],
                result["defence"],
                result["matches_played"],
                result["wins"],
                result["cup_wins"],
                result["bank_balance"],
                result["id"],
            )

                # Fetch players belonging to the team
            sql = "SELECT * FROM players WHERE team_id = %s"
            values = [id]
            player_results = run_sql(sql, values)
            players = [Player(  player_result["name"],
                                player_result["position"],
                                player_result["skill_level"],
                                team.name, 
                                player_result["team_id"], 
                                player_result["img_url"], 
                                player_result["id"]
                                ) 
                                for player_result in player_results] 

            team.players = players

        else:
            print("No results from select in team repo")
        
        return team
    else:
        print("None passed to select in team repo")


# remove a team from the league
def delete(id):
    sql = """
    DELETE FROM teams WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


# edit/update a team
def update(team):
    sql = """
    UPDATE teams SET (name, attack, defence, matches_played, wins, cup_wins, bank_balance) = (%s,%s,%s,%s,%s,%s,%s)
    WHERE id = %s
    """
    values = [
        team.name,
        team.attack,
        team.defence,
        team.matches_played,
        team.wins,
        team.cup_wins,
        team.bank_balance,
        team.id,
    ]
    run_sql(sql, values)


# update team stats after match result is known
def update_stats(team):
    sql = """
    UPDATE teams SET (matches_played, wins) = (%s, %s)
    WHERE id = %s
    """
    values = [team.matches_played, team.wins, team.id]
    run_sql(sql, values)


# delete all teams from the league
def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)
