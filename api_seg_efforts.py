####
#    Strava API - all segment efforts from all starred segments list  #
####

# workaround to interate and not encounter limit rate denial: temp download

# limit rate: split requests in 3 contigents of max 100 requests

# limits von strava: 100 requests every 15 min, max 2000 total per day

# hardcoded: starred_segments1, starred_segments2, starred_segments3 -> 

#               all_efforts1, all_efforts2, all_efforts3

# imports

import requests
import pandas as pd
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from access_token import personal_information

# Authentication payload , personal access token saved seperately
payload = personal_information

# List of segment IDs

df = pd.read_csv('starred_segments3.csv')
segment_id_list = df.drop(df.columns[[0]], axis=1).iloc[:, 0].tolist()
print(segment_id_list)

# test für datenbegrenzung
#segment_id_list = [13219413, 7463157, 4566096]

# URL for authentication and segments API
auth_url = "https://www.strava.com/oauth/token"  # Replace with actual URL
segments_url = "https://www.strava.com/api/v3/segment_efforts"

# getting a new access token through the refresh token

print("Requesting Token.....\n")
res = requests.post(auth_url, data= payload, verify=False)

access_token = res.json()['access_token']
print("Access Token = {}...\n".format(access_token))

# header

header = {'Authorization': 'Bearer ' + access_token}

# Loop for all activities if there are more than 200 activities
all_efforts = []

for segment_id in segment_id_list:
    page_num = 1
    total_pages = 1
    while page_num <= total_pages:
        params = {'per_page': 200, 'page': page_num, 'segment_id': segment_id}
        response = requests.get(segments_url, headers=header, params=params)
        data = response.json()
        print("Data:", data)
        
        if not data:
            print(f"Breaking out of while loop for segment ID {segment_id}, all activities are collected")
            break
        
        all_efforts.extend(data)
        page_num += 1
        total_pages = int(response.headers.get('X-Pagination-Total-Pages', 1))

# Save all_efforts to a JSON file on your desktop
output_file = 'all_efforts3.json'
with open(output_file, 'w') as f:
    json.dump(all_efforts, f, indent=4)

print(f"Data saved to {output_file}")


