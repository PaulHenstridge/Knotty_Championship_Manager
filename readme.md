# Knotty Championship Manager - Full Stack Sports League Simulation

A RESTful, full-stack application that simulates a sports league, using Python, Flask, and PostgreSQL.

## Overview

Create a team, buy and sell players, play matches, enter tournaments and rise to the top of the league!

A Python project built in the Model-View-Controller (MVC) pattern, with full CRUD functionlity and server rendered client.


## Features

- **Team Management**: Add, edit, or delete teams.
- **Player Management**: Add, edit, or delete players.
- **Transfer Market**: Buy and sell players, negotiate transfer fees.
- **Schedule and Play MAtches**: Set up and play matches.
- **Full Action Match Reports**:View match reports, including near misses and goal scorers.
- **Play Knockout Tournaments**:Teans play each other to win the Cup.
- **League Table**: Team standings in the league based on match results.
  
## Tech Stack

- **Back End**: Python and Flask
- **Database**: PostgreSQL
- **Front End**: Flask server-side rendered HTML, with CSS

## Getting Started

### Prerequisites

You should have the following installed:

- Python 3
- Flask
- PostgreSQL

### Installation

Clone the repo
```git clone https://github.com/PaulHenstridge/knotty_league```

Create the database
``` createdb knotty_league```

Run the sql file (from the root directory)
```psql -d knotty_league -f db/knotty_league.sql```

Start the application
```python3 app.py```

## Usage

A brief overview of how to use the application:
![league table](/static/images/Screenshot1.png)

- **Viewing league table**: '/teams' - teams are displayed in order of matches won. Select the 'info' icon to access team's info page.
- **Scheduling a match**: '/matches/new' - select participating teams to play one another.
- **Playing a match**: '/matches' - any scheduled matches not yet played will have a "Play Match" button.   Click this to play the match.
- **Viewing all a team's matches**: '/teams/{id}/matches' - choose "view matches" from the team's info page.  Displays all matches past and future involving team.
- **Adding a team**: '/teams/new' - input team name and attributes.
- **Removing a team**: '/teams/{id}/delete' - choose delete from the team's info page.
- **Editing a team's attributes**: '/teams/{id}/edit' - choose edit form team's info page. provide new value(s) for team attributes.

## Contributing

Contributions and collaborations are welcome. Please get in touch!

## License

This project is licensed under the MIT License.

## Contact

Paul Henstridge - paulhenstridge@gmail.com
Project Link: https://github.com/PaulHenstridge/knotty_league





