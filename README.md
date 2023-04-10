# Youtube Notifications Parser
Parse your Favorite Channels New Videos Titles Manually to your Notification System
 
 ## Requirements
1) Python 3.6 or higher
2) Dunst notification daemon 
3) `notify-send` utility
 
 ## Installation
1) Clone this repository to your local machine.
2) Install the required Python packages by running the following command in your terminal: 
`pip install -r requirements.txt`
3) Set up your list of Youtube channels in the UserNames and IconPaths variables in the script. `UserNames` is a list of the channel usernames you want to check, and `IconPaths` is a list of the corresponding paths to the icons you want to use for each channel.
4) Run the script in your terminal using the command: 
`python yt.py`
 
 ## How it Works
 The script makes a GET request to each channel's videos page and extracts the title and URL of the latest video. It then checks if the video title is already in a CSV file. If the video title is not in the CSV file, it sends a desktop notification with the video title and URL. The CSV file is used to keep track of which videos have already been viewed.
 
 `Also when you right click on the notification, it hyperlinks to the video URL`
 
 ## Note
Please note that Youtube does not officially support this type of parsing and may take action against accounts that use it. Use at your own risk.

 ## License
 This project is licensed under the GPL-3.0 license.
 
 ![ytscript](https://user-images.githubusercontent.com/69548206/230838226-6d20014a-0cd8-44c5-ab62-dd5c7e21f308.png)
