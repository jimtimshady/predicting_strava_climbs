# imports

import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from access_token import personal_information

# Authentication payload - > personal information saved in different file
payload = personal_information

# List of segment IDs from famous climbs: hardcoded
# IDs:
# 1.stelvio: 18663867
# 2. galibier: 18328881
# 3. mont ventoux: 7711822
# 4. alp d' huez: 13907878
# 5. col du tourmalet: 34128342
# 6. alto de letras: 12648314
# 7. teide: 707733
# 8. monte grappa: 611629
# 9. hawk hill: 12667647
# 10. brocken: 18051783

famous_segments_id = [18663867, 18328881, 7711822, 13907878, 34128342, 12648314, 707733, 611629, 12667647, 18051783]

# URL for authentication and segments API
auth_url = "https://www.strava.com/oauth/token"  # Replace with actual URL
segments_id_url = "https://www.strava.com/api/v3//segments/{id}"

# getting a new access token through the refresh token

print("Requesting Token.....\n")
res = requests.post(auth_url, data= payload, verify=False)

access_token = res.json()['access_token']
print("Access Token = {}...\n".format(access_token))

# header

header = {'Authorization': 'Bearer ' + access_token}

# Loop for all activities if there are more than 200 activities
famous_segments = []

for segment_id in famous_segments_id:
    page_num = 1
    total_pages = 1
    while page_num <= total_pages:
        params = {'per_page': 200, 'page': page_num}
         # Format the URL with the segment ID
        url = segments_id_url.format(id=segment_id) 
        response = requests.get(url, headers=header, params=params)
        data = response.json()
        print("Data:", data)
        
        if not data:
            print(f"Breaking out of while loop for segment ID {segment_id}, all activities are collected")
            break
        
        famous_segments.append(data)
        page_num += 1
        total_pages = int(response.headers.get('X-Pagination-Total-Pages', 1))

# Save all_efforts to a JSON file on your desktop
output_file = 'famous_segments.json'
with open(output_file, 'w') as f:
    json.dump(famous_segments, f, indent=4)

print(f"Data saved to {output_file}")
