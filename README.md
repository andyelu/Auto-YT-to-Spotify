#Auto-YT-to-Spotify
Auto-YT-to-Spotify is a powerful tool that automates the process of transferring the contents of a YouTube music playlist to your Spotify liked songs. With a few simple steps, you can seamlessly enjoy your favorite music across platforms. Follow the instructions below to get started:

Prerequisites
Spotify Access Token
To use the tool, you need to grab your Spotify access token. Here's how:

Create an app on Spotify Developer Dashboard.
Make a new app project and note down the client ID and secret client ID.
Set the redirect URI as your live server URL.
Open the index.html file using Live Server and paste the client ID and secret client ID.
Allow authorization to use your Spotify account.
After the redirect, press F12 (inspect element) and view your access token under the Application tab.
YouTube Credentials JSON File
Follow the instructions in this video (https://www.youtube.com/shorts/BBgrgA96n-Q?feature=share) to obtain the YouTube credentials JSON file. Ensure you add yourself as a Test User during this process. Otherwise, you will need to get the app verified to use it.

Set up 'creds' Directory
Place the YouTube credentials JSON file in a directory named 'creds'.

Installation and Setup
Install YouTube DL Library
If you encounter any issues during installation, run the following command to ensure the latest version of the YouTube DL library is installed:

bash
Copy code
pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/youtube-dl.git"
Run the Application
Open up your local terminal and follow the instructions below based on your system:

For Windows:
bash
Copy code
set SPOTIFY_AUTH_TOKEN=<YOUR_ACCESS_TOKEN>
For Unix-like systems (macOS, Linux):
bash
Copy code
export SPOTIFY_AUTH_TOKEN=<YOUR_ACCESS_TOKEN>
It will display a URL; visit that URL and log in to your YouTube account. Copy the provided item and paste it back into your terminal.

Usage
Once the setup is complete, you are all set to use Auto-YT-to-Spotify. Simply run the application, and it will automatically transfer the contents of your YouTube music playlist to your Spotify liked songs.

Contributing
We welcome contributions from the community! If you would like to contribute to the project, please follow the guidelines for pull requests, code formatting, and issue reporting mentioned in the CONTRIBUTING.md file.
