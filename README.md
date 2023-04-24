# Attribute Tagger

Attribute Tagger is a Python script that uses the Spotify API to fetch audio features and genres for MP3 files in your music library. The script then adds this information to the metadata of your MP3 files, allowing you to better categorize and understand your music collection.

## Features

- Fetch audio features and genres from the Spotify API
- Add audio features and genres to MP3 file metadata
- Select which attributes to include in the metadata
- Simple graphical user interface (GUI) for easy use

## Dependencies

The following Python libraries are required to run the Music Tagger:

- spotipy
- mutagen
- tkinter

## You can install these dependencies using pip:

pip install spotipy mutagen tkinter

python


## Setup

To set up the Music Tagger, you need to obtain Spotify API credentials, which include a client ID and a client secret. Follow these steps to get your API credentials:

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and log in with your Spotify account.
2. Click "Create an App" and fill in the required information.
3. Once your app is created, you'll see the client ID and client secret in the app's dashboard.

# How to edit the code to change the "default folder"

Open the main.py file in a code editor like VSC
Find the line default_folder = "/Users/Music/music-library" and replace the path with the path to your desired default folder.
Save the file.

## Usage

To run the Music Tagger, follow these steps:

1. Open a terminal or command prompt and navigate to the directory containing the `music_tagger.py` script.
2. Run the script:

python music_tagger.py


3. The Music Tagger GUI will open. Use the "Browse" button to select the folder containing your MP3 files.
4. Enter your Spotify API client ID and client secret in the corresponding text fields.
5. Select the audio features and genres you want to add to your MP3 files by checking the appropriate boxes.
6. Click the "Start" button to begin processing your MP3 files. The progress bar and progress entry field will display the progress of the operation.
7. Once the process is complete, the progress entry field will display "DONE".

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
