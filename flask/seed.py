from app import app
from models import db, Game

db.drop_all()
db.create_all()

g1 = Game(
    name='test1',
    min_players=1,
    max_players=10,
)
g2 = Game(
    name='test2',
    min_players=4,
)

db.session.add_all([g1,g2])
db.session.commit()