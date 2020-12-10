
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

  playlist = Playlist.query.get_or_404(playlist_id)
  form = NewSongForPlaylistForm()

  # Restrict form to songs not already on this playlist

  curr_on_playlist = [s.id for s in playlist.songs]
  form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all()))

  if form.validate_on_submit():

      # This is one way you could do this ...
      playlist_song = PlaylistSong(song_id=form.song.data,
                                  playlist_id=playlist_id)
      db.session.add(playlist_song)

      # Here's another way you could that is slightly more ORM-ish:
      #
      # song = Song.query.get(form.song.data)
      # playlist.songs.append(song)

      # Either way, you have to commit:
      db.session.commit()

      return redirect(f"/playlists/{playlist_id}")

  return render_template("add_song_to_playlist.html",
                         playlist=playlist,
                         form=form)