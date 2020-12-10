from flask import Flask, redirect, render_template, session, flash, request, Response
from flask_debugtoolbar import DebugToolbarExtension
# from flask_psycopg2 import 
from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
app.config["WTF_CSRF_ENABLED "]= False
# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route("/")
def root():
    return redirect("/playlists")

##############################################################################
# Playlist routes

@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    return render_template("playlists.html")


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    form = NewSongForPlaylistForm()
    playlistID = Playlist.query.get(playlist_id)
    
    return render_template("playlists.html", playlists=playlistID, form=form )


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form =  PlaylistForm()

    if form.validate_on_submit():
        name= form.name.data  
        description = form.description.data
        new_playlist= Playlist(id=id,name=name,description=description)
        db.session.add(new_playlist)
        db.session.commit()
        print(session,new_playlist)
        return redirect(f'playlists/{new_playlist.id}/add-song')

    return render_template('new_playlist.html', form=form)  
 


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    curr_on_playlist =[s.id for s in playlist.songs]
    print(curr_on_playlist)

    if form.validate_on_submit():
        # song = Song.query.get(form.song.data)
        # playlist.songs.append(song)
        playlist_song = Song(song_title=form.title.data, song_artitst=form.artist.data)
        db.session.add(playlist_song)
        db.session.commit()
        return redirect(f'/playlists/{playlist_id}')

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
      
    # return render_template("new_playlist.html", form=form)
##############################################################################
# Song routes

@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    songs = Song.query.all() 
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    if 'song' in session:
        return redirect("/songs")
    #song=Song.query.all()
    form =SongForm()
    if form.validate_on_submit():
        title= form.title.data
        artist = form.artist.data
        new_song= Song(title=title, artist=artist)
        db.session.add(new_song)
        db.session.commit()
        return redirect('/playlists')



