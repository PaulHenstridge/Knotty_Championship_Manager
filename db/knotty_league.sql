DROP TABLE IF EXISTS transfers;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    attack INT,
    defence INT,
    matches_played INT,
    wins INT,
    bank_balance INT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    team1_id INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    team2_id INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    completed BOOLEAN,
    winner_id INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(50),
    skill_level INT,
    team_id INT NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    img_url VARCHAR(255)
);

CREATE TABLE transfers (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id),
    team_from_id INT REFERENCES teams(id) ON DELETE CASCADE,
    team_to_id INT REFERENCES teams(id)  ON DELETE CASCADE,
    transfer_fee INT,
    status VARCHAR(20)
);

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
    winner INTEGER NULL
);

CREATE TABLE tournament_teams (
    tournament_id INTEGER,
    team_id INTEGER,
    PRIMARY KEY (tournament_id, team_id),
    FOREIGN KEY (tournament_id) REFERENCES tournaments(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);




INSERT INTO teams (name, attack, defence, matches_played, wins, bank_balance) 
VALUES ('Lybster', 75, 25, 1, 1, 5000);

INSERT INTO teams (name, attack, defence, matches_played, wins, bank_balance) 
VALUES ('Dunbeath', 55, 85, 1, 0, 5000);

INSERT INTO teams (name, attack, defence, matches_played, wins, bank_balance) 
VALUES ('Kiess', 45, 55, 0, 0, 5000);

INSERT INTO matches (team1_id, team2_id, completed, winner_id)
VALUES (1,2,'t',1);

INSERT INTO players (name, position, skill_level, team_id, img_url) 
VALUES ('John Doe', 'Attacker', 80, 1, Null);

INSERT INTO players (name, position, skill_level, team_id, img_url) 
VALUES ('Jack Doe', 'Defender', 60, 1, Null);

INSERT INTO players (name, position, skill_level, team_id, img_url) 
VALUES ('Jim Doe', 'Attacker', 50, 2, Null);

INSERT INTO players (name, position, skill_level, team_id, img_url) 
VALUES ('George Doe', 'Defender', 70, 2, Null);
