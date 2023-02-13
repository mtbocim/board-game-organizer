from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database"""

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Game(db.Model):
    """Properties of a boardgame"""

    __tablename__ = "boardgames"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement = True,
    )
    
    name = db.Column(
        db.String(30),
        nullable = False
    )

    def serialize(self):
        """Serialize to dicitionary"""

        return {
            "id": self.id,
            "name": self.name,
        }