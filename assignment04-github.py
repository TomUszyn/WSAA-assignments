"""
# This script updates a file in a GitHub repository by replacing 'Andrew' with 'Tomasz'.
"""
# Author: Tomasz Uszynski

import base64
import requests
from config import config as cfg

# GitHub settings
URL = 'https://api.github.com/repos/TomUszyn/WSAA-ASSIGNMENTS/contents/Step_by_step.txt'
apiKey = cfg["githubk"]
TIMEOUT = 10  # Timeout for requests in seconds

# Fetch the file content from GitHub
response = requests.get(URL, auth=('token', apiKey), timeout=TIMEOUT)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    if "content" in data and "sha" in data:
        content = base64.b64decode(data["content"]).decode("utf-8")
        sha = data["sha"]
        
        
        # Modify content and re-encode
        modifiedContent = content.replace("Andrew", "Tomasz")
        encodedContent = base64.b64encode(modifiedContent.encode("utf-8")).decode("utf-8")
        
        # Prepare the update request
        updateData = {
            "message": "Replaced 'Andrew' with 'Tomasz'",
            "content": encodedContent,
            "sha": sha,
        }

        # Commit the changes
        updateResponse = requests.put(URL, auth=('token', apiKey), json=updateData, timeout=TIMEOUT)

        if updateResponse.status_code in [200, 201]:
            print("File updated successfully!")
        else:
            print(f"Error updating file: {updateResponse.status_code}, {updateResponse.json()}")

    else:
        print("Error: Missing 'content' or 'sha' in the response")
    
else:
    print(f"Error fetching file: {response.status_code}, {response.json()}")

