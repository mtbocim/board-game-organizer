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

@app.get('/api/games/<int:game_id>')
def list_single_game(game_id):
    """Get data about a single game
    
    Return JSON {....}
    
    Raise 404 error if game cannot be found

    Args:
        game_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    game = Game.query.get_or_404(game_id)
    serialized = game.serialize()
    
    return jsonify(game=serialized)

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

@app.patch('/api/games/<int:game_id>')
def patch_game_info(game_id):
    """Patch information about a game
    
    Raise 404 if not found

    Args:
        game_id (_type_): _description_
    """
    
    data = request.json
    
    game = Game.query.get_or_404(game_id)
    
    game.name = data.get("name", game.name)
    
    db.session.add(game)
    db.session.commit()
    
    serialized = game.serialize()
    return jsonify(game=serialized)

@app.delete('/api/games/<int:game_id>')
def delete_game_info(game_id):
    """Delete game
    
    Raise 404 if game cannot be found
    Return confirmation of deletion as JSON {}

    Args:
        game_id (_type_): _description_
    """
    
    game = Game.query.get_or_404(game_id)
    
    db.session.delete(game)
    db.session.commit()
    
    return jsonify(deleted=game_id)