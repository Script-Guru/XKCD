
#python 2.7
#retrieve the json resource from xkcd and download
#the daily comic

import urllib, json
url = "https://xkcd.com/info.0.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
#newimage=(data['img'])

fileString=(str(data['num']) + " " + data['title'] + ".png")
urllib.urlretrieve(data['img'], fileString)
print("'" + fileString + "'" + " downloaded from " + "https://xkcd.com/")
