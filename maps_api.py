import requests
import json
from token_call import get_token
import pprint
pp = pprint.PrettyPrinter(indent=3)

def find_directions(home_address, testing_address):
# AIzaSyCoT_XZYJHOk46SQL8h5A8qDQ1-mokZdVEw
# url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=YOUR_API_KEY"
# origin=24+Sussex+Drive+Ottawa+ON

    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + "Stonehedge+Drive+South+Burlington+VT" + "&destination=" + "Montreal? " + "&key=AIzaSyCoT_XZYJHOk46SQL8h5A8qDQ1-mokZdVE"

    #url = "https://google-maps28.p.rapidapi.com/maps/api/directions/json"

    #querystring = {"destination": testing_address, "origin": home_address,
    #               "language": "en", "region": "en"}

    headers = {
      #  "X-RapidAPI-Key": "aa436d09d1mshbf379606b79362dp1af3ddjsnbfbb9da35be9",
       # "X-RapidAPI-Host": "google-maps28.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params={})

    print(response.text)
find_directions("x","y")