Attribute Tagger

Attribute Tagger is an advanced Python application, brought to life with the guidance of OpenAI's ChatGPT 4. This tool serves as a bridge between your MP3 music library and the Spotify API, fetching insightful audio features and genres for your music tracks and integrating this data directly into each file's metadata. The result is a richer, more informative music collection that can be categorized and explored in new and exciting ways.

Key Features

Leverages the Spotify API to retrieve a wide range of audio features and genres for each MP3 track.
Seamlessly integrates the retrieved data into the metadata of the corresponding MP3 files.
Allows for customization of the attributes to be included in the metadata.
Provides an intuitive Graphical User Interface (GUI) designed for ease of use.
Prerequisites

Attribute Tagger relies on the following Python libraries:

spotipy
mutagen
tkinter
To install these dependencies, use pip:

bash
Copy code
pip install spotipy mutagen tkinter
Getting Started

Before using Attribute Tagger, you'll need to acquire Spotify API credentials. Here's a step-by-step guide to obtaining your client ID and client secret:

Visit the Spotify Developer Dashboard and log in to your Spotify account.
Click "Create an App" and complete the required fields.
Once your app is set up, your client ID and client secret will be displayed on the app's dashboard.
Configuring the Default Folder

Attribute Tagger, by default, searches for MP3 files in a preset folder. To modify this:

Open the music_tagger.py file in a code editor.
Locate the line default_folder = "/Users/Music/music-library".
Replace "/Users/Music/music-library" with the path to your preferred default folder.
Save the changes.
Usage

Running Attribute Tagger is straightforward:

Open a terminal or command prompt and navigate to the directory where the music_tagger.py script is located.
Run the script: python music_tagger.py
The GUI will open. Use the "Browse" button to select your MP3 folder.
Input your Spotify API client ID and client secret in the appropriate fields.
Check the boxes next to the audio features and genres you wish to add to your MP3 files.
Click "Start" to initiate the process. The progress bar and text field will keep you updated on the operation's progress.
When completed, the text field will display "DONE".
This application was developed with significant assistance from ChatGPT 4. This highly advanced language model by OpenAI provided valuable insights, suggestions, and guidance throughout the development process.

Contributions

We greatly appreciate contributions from the community. Please feel free to submit pull requests. If you have major changes in mind, we encourage you to open an issue first to discuss your proposed changes. Please ensure that you update or create tests as appropriate.

License

Attribute Tagger is licensed under the MIT License.
