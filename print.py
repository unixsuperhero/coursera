import urllib
import json

for page in range(1,10):
  response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
  d = json.load(response)
  for t in d['results']:
    print t['text']

