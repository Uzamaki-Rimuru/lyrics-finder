import lyricsgenius
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace 'YOUR_TOKEN_HERE' with your actual Genius API token
genius = lyricsgenius.Genius(
    "TBZI86mxyRwI_VTtWkVZZ0VCrSlV1p-RVxNZEjOnEgd-ZeIFkbmfWfLrylPRL6qj")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def get_real_lyrics():
    data = request.json
    song_name = data.get('topic')  # The user types the song name here

    try:
        # This searches the Genius database for the song
        song = genius.search_song(song_name)
        if song:
            return jsonify({"result": song.lyrics})
        else:
            return jsonify({"result": "Song not found. Check the spelling!"})
    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/generate', methods=['POST'])
def get_real_lyrics():
    data = request.json
    song_query = data.get('topic')  # What the user typed

    if not song_query:
        return jsonify({"result": "Please enter a song name!"})

    try:
        # We use search_song to find the best match
        print(f"Searching for: {song_query}")
        song = genius.search_song(song_query)

        if song:
            # Successfully found!
            return jsonify({"result": f"Title: {song.title}\nArtist: {song.artist}\n\n{song.lyrics}"})
        else:
            # Genius returned nothing
            return jsonify({"result": "I couldn't find that song. Try adding the artist name (e.g., 'Hello Adele')."})

    except Exception as e:
        # This catches internet issues or API errors
        print(f"Server Error: {e}")
        return jsonify({"result": "Oops! There was a connection error. Please try again in a moment."})

        # Change your existing line to this:
        # We increase the timeout to 15 seconds and add 3 retries
    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, timeout=15, retries=3)

    if song:
        return jsonify({
            "result": song.lyrics,
            "image": song.song_art_image_url,
            "title": song.title,
            "artist": song.artist
        })


@app.route('/mood', methods=['POST'])
def recommend_by_mood():
    data = request.json
    user_mood = data.get('topic').lower()  # Get the mood and make it lowercase

    # This is a Python Dictionary - our local 'database'
    playlists = {
        "happy": "1. Walking on Sunshine - Katrina & The Waves\n2. Happy - Pharrell Williams\n3. Don't Stop Me Now - Queen",
        "sad": "1. Someone Like You - Adele\n2. Fix You - Coldplay\n3. Yesterday - The Beatles",
        "energetic": "1. Eye of the Tiger - Survivor\n2. Power - Kanye West\n3. Thunderstruck - AC/DC"
    }

    # Check if we have songs for that mood
    result = playlists.get(
        user_mood, "I don't have a playlist for that mood yet. Try 'happy', 'sad', or 'energetic'!")

    return jsonify({"result": result})
