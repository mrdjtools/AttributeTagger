import os
import sys
import tkinter as tk
from tkinter import filedialog
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, COMM
from mutagen.mp3 import MP3
import glob
import time
import threading
from tkinter import ttk
import requests
from requests.exceptions import RequestException


def authenticate_spotify(client_id, client_secret):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_audio_features(spotify, track_name):
    try:
        results = spotify.search(q=track_name, type='track', limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            audio_features = spotify.audio_features([track['id']])[0]

            if audio_features is not None:
                # Get artist's genres
                artist = spotify.artist(track['artists'][0]['id'])
                genres = artist['genres']

                # Add genres to the audio_features dictionary
                audio_features['genres'] = ', '.join(genres)

                return audio_features
    except requests.exceptions.ReadTimeout:
        print(f"ReadTimeout error when retrieving audio features for {track_name}. Retrying...")
        time.sleep(2)
        return get_audio_features(spotify, track_name)
    except RequestException as e:
        print(f"Error retrieving audio features for {track_name}: {str(e)}")
        return None
    return None



def update_comment_with_features(audio, features, file_ext):
    if file_ext == '.mp3':
        audio_tags = ID3(audio.filename)

        # Update genre information
        if 'genres' in features:
            audio_tags['TCON'] = mutagen.id3.TCON(encoding=3, text=features['genres'])

        # Update comment section with other features
        comment = audio_tags.getall('COMM')
        if comment:
            comment = comment[0]
        else:
            comment = COMM(encoding=3, lang='eng', desc='')
            audio_tags.add(comment)

        comment_text = ""
        for feature, value in features.items():
            if feature != 'genres':
                comment_text += f" {feature.capitalize()}: {value};"

        comment.text = comment_text.strip()
        audio_tags.save()
    else:
        pass


def main(music_folder, client_id, client_secret, selected_attributes, progress_var, progress_bar):
    spotify = authenticate_spotify(client_id, client_secret)

    files_to_process = []
    for root, _, files in os.walk(music_folder):
        for file in files:
            if file.lower().endswith(".mp3"):
                files_to_process.append(os.path.join(root, file))

    progress_bar["maximum"] = len(files_to_process)

    for index, file_path in enumerate(files_to_process):
        progress_var.set(file_path)
        progress_bar["value"] = index + 1
        try:
            audio = MP3(file_path, ID3=ID3)
        except mutagen.mp3.HeaderNotFoundError as e:
            print(f"Error processing {file_path}: {str(e)}")
            continue

        track_name = os.path.splitext(os.path.basename(file_path))[0]
        audio_features = get_audio_features(spotify, track_name)
        if audio_features:
            filtered_features = {attr: audio_features[attr] for attr in selected_attributes}
            update_comment_with_features(audio, filtered_features, '.mp3')
        else:
            print(f"Skipping {track_name} due to missing audio features")
        time.sleep(0.1)

    progress_var.set("DONE")



def run_gui():
    default_folder = "/Users/Music/music-library"

    def start_processing():
        music_folder = folder_entry.get()
        client_id = client_id_entry.get()
        client_secret = client_secret_entry.get()
        selected_attributes = [attr for attr, var in attribute_vars.items() if var.get()]

        processing_thread = threading.Thread(target=main, args=(music_folder, client_id, client_secret, selected_attributes, progress_var, progress_bar))
        processing_thread.start()

    def browse_folder():
        folder = filedialog.askdirectory(initialdir=default_folder)  # Add initialdir parameter here
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder)

    root = tk.Tk()
    root.title("Music Tagger")

    main_frame = tk.Frame(root, padx=10, pady=10)
    main_frame.pack()

    folder_frame = tk.Frame(main_frame)
    folder_frame.pack(pady=5)

    folder_label = tk.Label(folder_frame, text="Music Folder:")
    folder_label.pack(side=tk.LEFT)
    folder_entry = tk.Entry(folder_frame, width=50)
    folder_entry.pack(side=tk.LEFT, padx=5)
    browse_button = tk.Button(folder_frame, text="Browse", command=browse_folder)
    browse_button.pack(side=tk.LEFT)

    client_id_label = tk.Label(main_frame, text="Client ID:")
    client_id_label.pack(pady=5, anchor='w')
    client_id_entry = tk.Entry(main_frame, width=50)
    client_id_entry.pack()

    client_secret_label = tk.Label(main_frame, text="Client Secret:")
    client_secret_label.pack(pady=5, anchor='w')
    client_secret_entry = tk.Entry(main_frame, width=50)
    client_secret_entry.pack()

    attributes_label = tk.Label(main_frame, text="Attributes:")
    attributes_label.pack(pady=5, anchor='w')

    attributes_frame = tk.Frame(main_frame)
    attributes_frame.pack()

    attribute_vars = {
        "danceability": tk.BooleanVar(),
        "energy": tk.BooleanVar(),
        "key": tk.BooleanVar(),
        "loudness": tk.BooleanVar(),
        "mode": tk.BooleanVar(),
        "speechiness": tk.BooleanVar(),
        "acousticness": tk.BooleanVar(),
        "instrumentalness": tk.BooleanVar(),
        "liveness": tk.BooleanVar(),
        "valence": tk.BooleanVar(),
        "tempo": tk.BooleanVar(),
        "genres": tk.BooleanVar(),
    }

    for index, (attr, var) in enumerate(attribute_vars.items()):
        chk = tk.Checkbutton(attributes_frame, text=attr.capitalize(), variable=var)
        chk.grid(row=index // 4, column=index % 4, padx=5, pady=5)

    start_button = tk.Button(main_frame, text="Start", command=start_processing)
    start_button.pack(pady=10)

    progress_label = tk.Label(main_frame, text="Progress:")
    progress_label.pack(pady=5, anchor='w')
    progress_var = tk.StringVar()
    progress_var.set("Not started")
    progress_entry = tk.Entry(main_frame, width=50, textvariable=progress_var, state='readonly')
    progress_entry.pack()

    progress_bar = ttk.Progressbar(main_frame, mode='determinate')
    progress_bar.pack(pady=5, fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
