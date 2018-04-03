import sys
sys.path.insert(0, '..')
import gemini
import urllib2
base_url = "https://api.gemini.com/v1"
# or, for sandbox
# base_url = "https://api.sandbox.gemini.com/v1"
response = urllib2.urlopen(base_url + "/symbols")
print(response.read())
print('dv')
