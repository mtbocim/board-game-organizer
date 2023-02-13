from app import app
from models import db, Game

db.drop_all()
db.create_all()

g1 = Game(
    name='test1'
)
g2 = Game(
    name='test2'
)

db.session.add_all([g1,g2])
db.session.commit()