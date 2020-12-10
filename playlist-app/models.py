from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

bcrypt = Bcrypt()
db = SQLAlchemy()



class Playlist(db.Model):
    __tablename__= "playlists"
    # ADD THE NECESSARY CODE HERE
    id=db.Column(db.Integer,primary_key=True,unique=True, autoincrement=True,)
    name=db.Column(db.String(30), nullable=False)
    description=db.Column(db.Text, nullable=False)
    Song= db.relationship('Song')
    #@classmethod
    # def make_playlist(cls,name,description):
    #     new_playlist= cls( 
    #     name=name, description=description)
    #     db.session.add(new_playlist)
    #     return new_playlist


class Song(db.Model):
    __tablename__="songs"
    # ADD THE NECESSARY CODE HERE
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.Text,nullable=False)
    artist=db.Column(db.Text,nullable=False)
    playlist= db.relationship("Playlist")


class PlaylistSong(db.Model):
    __tablename__="playlist_songs"
    # ADD THE NECESSARY CODE HERE
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    playlist_id= db.Column(db.Integer,nullable=False)
    song_id= db.Column(db.Integer,nullable=False)

    playlist= db.relationship('Playlist')
    Song= db.relationship('Song')

def connect_db(app):
    db.app = app
    db.init_app(app)
