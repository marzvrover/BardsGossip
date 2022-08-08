#!/usr/local/bin/python3

import argparse
from bs4 import BeautifulSoup
import importlib
import json
import requests
import sys

# import pyperclip for non-pythonista and clipboard for pythonista
PYPERCLIP = importlib.util.find_spec("pyperclip")
CLIPBOARD = importlib.util.find_spec("clipboard")

if PYPERCLIP != None:
  import pyperclip
elif CLIPBOARD != None:
  import clipboard

API_URI = "https://songwhip.com/"
source_uri = "https://open.spotify.com/track/5YxtCGHvn9oE43NM9Hh5VE?si=b85zlpa8SA6CswoWRLUCXw"

def fetchLinks(apiURI, sourceURI):
  data_json = {"url": sourceURI}

  request = requests.Request("POST", apiURI)
  request.data = json.dumps(data_json)

  session = requests.Session()
  songwhip = session.send(request.prepare()).json()

  response = requests.request("GET", songwhip["url"])
  soup = BeautifulSoup(response.content, "html5lib")
  songwhip_content = json.loads(soup.select("script#__NEXT_DATA__")[0].contents[0])

  return songwhip_content["props"]["initialReduxState"]["tracks"][str(songwhip["id"])]["value"]["links"]

def getAmazonMusicLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["amazonMusic"][0]["link"]

def getAppleMusicLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  templatedLink = links["itunes"][0]["link"]
  return templatedLink.replace("{country}", "US")

def getDeezerLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["deezer"][0]["link"]

def getNapsterLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["napster"][0]["link"]

def getPandoraLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["pandora"][0]["link"]

def getQobuzLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["qobuz"][0]["link"]

def getSongwhipLink(apiURI, sourceURI):
  data_json = {"url": sourceURI}

  request = requests.Request("POST", apiURI)
  request.data = json.dumps(data_json)

  session = requests.Session()
  return session.send(request.prepare()).json()["url"]

def getSpotifyLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["spotify"][0]["link"]

def getTidalLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["tidal"][0]["link"]

def getYouTubeLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["youtube"][0]["link"]

def getYouTubeMusicLink(apiURI, sourceURI):
  links = fetchLinks(apiURI, sourceURI)
  return links["youtubeMusic"][0]["link"]

def main():
  args = parseArgs()
  link = findLink(args)
  if args.silent == False:
    print(link)
  if args.copy == True:
    copyToClipboard(link)

def parseArgs():
  parser = argparse.ArgumentParser(description="Convert your music links to other music services")
  parser.add_argument("url", nargs=1, help="The URL of the song you want to convert")
  parser.add_argument("--copy", action="store_true", help="Copy the link to your clipboard")
  parser.add_argument("--silent", action="store_true", help="Don't print the link")
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument("--amazon-music", action="store_true", help="Get the Amazon Music link")
  group.add_argument("--apple-music", action="store_true", help="Get the Apple Music link")
  group.add_argument("--deezer", action="store_true", help="Get the Deezer link")
  group.add_argument("--napster", action="store_true", help="Get the Napster link")
  group.add_argument("--pandora", action="store_true", help="Get the Pandora link")
  group.add_argument("--qobuz", action="store_true", help="Get the Qobuz link")
  group.add_argument("--songwhip", action="store_true", help="Get the SongWhip link")
  group.add_argument("--spotify", action="store_true", help="Get the Spotify link")
  group.add_argument("--tidal", action="store_true", help="Get the Tidal link")
  group.add_argument("--youtube", action="store_true", help="Get the YouTube link")
  group.add_argument("--youtube-music", action="store_true", help="Get the YouTube Music link")
  return parser.parse_args()

def findLink(args):
  if args.amazon_music == True:
    return getAmazonMusicLink(API_URI, args.url)
  elif args.apple_music == True:
    return getAppleMusicLink(API_URI, args.url)
  elif args.deezer == True:
    return getDeezerLink(API_URI, args.url)
  elif args.napster == True:
    return getNapsterLink(API_URI, args.url)
  elif args.pandora == True:
    return getPandoraLink(API_URI, args.url)
  elif args.qobuz == True:
    return getQobuzLink(API_URI, args.url)
  elif args.songwhip == True:
    return getSongwhipLink(API_URI, args.url)
  elif args.spotify == True:
    return getSpotifyLink(API_URI, args.url)
  elif args.tidal == True:
    return getTidalLink(API_URI, args.url)
  elif args.youtube == True:
    return getYouTubeLink(API_URI, args.url)
  elif args.youtube_music == True:
    return getYouTubeMusicLink(API_URI, args.url)

def copyToClipboard(link):
  if PYPERCLIP != None:
    pyperclip.copy(link)
  elif CLIPBOARD != None:
    clipboard.set(link)
  else:
    print("No clipboard found", file=sys.stderr)
    exit(1)

main()
