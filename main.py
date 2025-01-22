import requests
import json

# Fetch the HTML content of the YouTube video page
r = requests.get("https://youtu.be/a-Nh25KebHQ?si=e0PJ2ll5S1xfpNR7")

# Split the HTML content at the "captions" keyword to isolate the relevant JSON block
split = r.text.split('"captions":')
   
captions_json = json.loads(
    split[1].split(',"videoDetails')[0].replace("\n", "")
    ).get("playerCaptionsTracklistRenderer")

print(captions_json)
url_captions = captions_json["captionTracks"][0]['baseUrl'].split("'name':")[0]
print(url_captions)
print(requests.get(url_captions).text)
