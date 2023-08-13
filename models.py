from flask_sqlalchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

def connect_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Available pet."""

    __tablename__= "pets"

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.Text, nullable=False)
    species   = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age       = db.Column(db.Integer)
    notes     = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE