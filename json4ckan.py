import urllib
import json

site = 'http://data.jrc.ec.europa.eu/api/3/action/package_search?q='
search1 = raw_input('Enter search: ')

search = search1.replace(' ', '+')

url = site + '"' + search + '"'

print 'Retrieving', url
response = urllib.urlopen(url).read()
info = json.loads(str(response))

t=info['result']['results']

for item in t:
    print 'ID', item['name']
