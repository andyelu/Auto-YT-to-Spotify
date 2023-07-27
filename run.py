import os

from spotify_client import SpotifyClient
from youtube_client import YouTubeClient

def run():
    # get array of playlists from YouTube
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlists()

    # determine what playlist we want music from
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    # get song information from the videos
    songs = youtube_client.get_videos_from_playlists(chosen_playlist.id)
    print(f"Attempting to add {len(songs)}")

    # search for songs on spotify
    for song in songs:
        spotify_song_id = spotify_client.search_songs(song.artist, song.track)
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify(spotify_song_id)
            if added_song:
                print(f"Added {song.artist}")


if __name__ == '__main__':
    run()