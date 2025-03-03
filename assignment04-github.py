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
    print(response.status_code)
    data = response.json()
    print(data["content"])
else:
    print(f"Error fetching file: {response.status_code}, {response.json()}")

