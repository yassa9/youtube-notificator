# GPL-3.0 license | Yassa Seifen

import requests
import time 
import subprocess
import re
import csv

# Define the paths
csv_path = "/home/yassa/.scripts/yt/csvpy.csv"
ip = "/home/yassa/.scripts/yt/icons" 

# List of channel usernames to check
UserNames = ['Sport360Arabiya','erza3ma3serry','DOCTOR-CHESS','salahgooda','Pharmastan','Saba7oKorah','Badr3','MZRecordsTopMusicAzerbaijan','bigthink']
IconPaths = ['loay.jpg','erz3.jpg','nofal.ico','salah.jpg','pharma.png','sba7o.jpg','badr.jpg','music.jpg','bigthink.jpg']

new_videos_added = False  # Flag to check if any new videos were added

for username, icon in zip(UserNames, IconPaths):
    # Make a GET request to the channel's videos page
    response = requests.get(f"https://www.youtube.com/@{username}/videos")
    html_code = response.content.decode('utf-8')
    
    # Assuming the HTML source code is stored in a variable called "html_code"
    match = re.search(r'"title":{"runs":\[\{"text":"(.+?)"\}\],"accessibility":{"accessibilityData"', html_code)
    title_text = match.group(1)

    match2 = re.search(r'/watch\?v=([^\"]+)', html_code)
    title_url = match2.group(1)
    clean_url = re.sub(r"[{}']", "", title_url)

    # Read the CSV file into a list of rows
    with open(csv_path, mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    # Check if the title is in the CSV file
    if any(title_text in row for row in rows):
        # Title is already in the CSV file
        print("Video title is already viewed")
        
    else:
        # Title is not in the CSV file
        with open(csv_path, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([title_text])

        link = f"/home/yassa/.scripts/yt/icons/{icon}"
        message = f"<span foreground='red' font='Monospace 1'>https://www.youtube.com/watch?v={clean_url}</span>"
        subprocess.run(["notify-send", title_text, message, "--icon", link, "-h", f"string:x-canonical-private-synchronous:video_id={clean_url}"], check=True)
        new_videos_added = True

if not new_videos_added:
    command = f"notify-send  --icon={ip}/ytlogo.png 'No Youtube Updates' \n"
    subprocess.call(command,  shell=True)  