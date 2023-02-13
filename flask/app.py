from crypt import methods
from flask import Flask, jsonify, request, render_template

from models import db, connect_db, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///games'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = 'no'

@app.get('/api/games')
def list_all_games():
    """
    Get information about all games

    Return JSON {}
    """

    #TODO: Write out proper JSON return details

    games = Game.query.all()
    serialized = [g.serialize() for g in games]

    return jsonify(games=serialized)

@app.post('/api/games')
def add_new_game():
    """
    Add new game to database

    """

    name = request.json["name"]

    new_game = Game(
        name=name,
    )

    db.session.add(new_game)
    db.session.commit()

    serialized = new_game.serialize()

    return (jsonify(game=serialized), 201)