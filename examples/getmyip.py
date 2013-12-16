import requests

r = requests.get('http://httpbin.org/ip')
origin = r.json['origin']

print "My IP address is:", origin
