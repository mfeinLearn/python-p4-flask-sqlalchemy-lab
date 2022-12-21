from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Zookeeper(db.Model):
    # [x]name, a [x]birthday, and a list of [x]animals that they take care of.
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.DateTime)
    animals = db.relationship('Animal', backref=backref('zookeeper'))

#db.session.query(Animal).count()
class Enclosure(db.Model):
    #  [x]environment (grass, sand, or water), an [x]open_to_visitors boolean, and a [x]list of animals.
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean, default=False)
    animals = db.relationship('Animal', backref=backref('enclosure'))

class Animal(db.Model):
    # [x]name, a [x]species, a [x]zookeeper, and an [x]enclosure
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
