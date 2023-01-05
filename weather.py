import sys
import requests

url = "https://wttr.in"
response = requests.get( url + "/" + sys.argv[1].replace(" ", "+"))
print(response.text)
