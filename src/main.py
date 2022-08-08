import requests
import json
from bs4 import BeautifulSoup

API_URI = "https://songwhip.com/"
source_uri = "https://open.spotify.com/track/5YxtCGHvn9oE43NM9Hh5VE?si=b85zlpa8SA6CswoWRLUCXw"

def getLinks(apiURI, sourceURI):
	data_json = {"url": sourceURI}

	request = requests.Request("POST", apiURI)
	request.data = json.dumps(data_json)

	session = requests.Session()
	songwhip = session.send(request.prepare()).json()

	response = requests.request("GET", songwhip["url"])
	soup = BeautifulSoup(response.content, "html5lib")
	songwhip_content = json.loads(soup.select("script#__NEXT_DATA__")[0].contents[0])

	return songwhip_content["props"]["initialReduxState"]["tracks"][str(songwhip["id"])]["value"]["links"]

def getAppleMusicLink(apiURI, sourceURI):
	links = getLinks(apiURI, sourceURI)
	templatedLink = links["itunes"][0]["link"]
	return templatedLink.replace("{country}", "US")

def getSpotifyLink(apiURI, sourceURI):
	links = getLinks(apiURI, sourceURI)
	return links["spotify"][0]["link"]

print(getAppleMusicLink(API_URI, source_uri))
print(getSpotifyLink(API_URI, source_uri))