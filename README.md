# Auto-YT-to-Spotify
Automates the process of transferring the contents of a YouTube music playlist to your Spotify liked songs

Grab your Spotify access token by first creating an app on Spotify Developer. Make a new app project (the redirect URI should be your live server url; here you can view your client id and secret client id.
Then open the index.html with Live Server. Paste the client id and secret client id in. Allow authorization to use your spotify account. After the redirect, press F12 (inspect element) and view your access token under the Application tab.

Then install the youtube credentials json file following these instructions: https://www.youtube.com/shorts/BBgrgA96n-Q?feature=share.
While you are doing this, add yourself as a Test User. Otherwise you need to get the app verified to be able to use it. 

Place the file in the a 'creds' directory.

To run, open up the local terminal. Type in: 

**set SPOTIFY_AUTH_TOKEN=<YOUR_ACCESS_TOKEN>**

For Unix-like systems, including macOS and Linux

**export SPOTIFY_AUTH_TOKEN=<YOUR_ACCESS_TOKEN>**

It will return:

**Please visit this URL to authorize this application:**

Visit that URL and login to your YouTube account. Copy the item it provides you and paste it back into your terminal.
