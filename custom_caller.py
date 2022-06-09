import requests
import requests.auth
import oauthlib
import requests_oauthlib
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

url = "https://api.preview.platform.athenahealth.com/v1/60768719/reference/order/lab?searchvalue=voluptate ad"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer A3zJAY5J4PUY0rnAeofhaZL1fzEw'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

#token_url = "https://api.preview.platform.athenahealth.com/oauth2/v1/token"
#client_id = r'0oadb13vj80mhxaAx297'
#client_secret = r'MqxSqyVY-ziputtp2X5TH-osS25qcPV2WkKDgtJB',
#client = BackendApplicationClient(client_id=client_id)
#oauth = OAuth2Session(client=client)
#token = oauth.fetch_token(token_url='https://api.preview.platform.athenahealth.com/oauth2/v1/token', client_id=client_id,
      #  client_secret=client_secret)

#print(token)
#grant_type = "client_credentials"
#scope = 'athena/service/Athenanet.MDP.*'
#URL = "https://api.preview.platform.athenahealth.com/v1/:practiceid/chart/encounter/:encounterid/orders/lab"
#response = requests.post(URL, auth=(client_id, client_secret),data={'grant_type':grant_type,'client_id':client_id,'client_secret':client_secret,'scope':scope,'token_url':token_url})

#print(response)
token_url = "https://api.preview.platform.athenahealth.com/oauth2/v1/token"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {'grant_type=client_credentials'.encode(), 'scope=athena/service/Athenanet.MDP.*'.encode()}

token = requests.post('https://api.preview.platform.athenahealth.com/oauth2/v1/token', headers=headers, data=data, auth=('$0oadb13vj80mhxaAx297', '$MqxSqyVY-ziputtp2X5TH-osS25qcPV2WkKDgtJB'))
print(token)






url = "https://api.preview.platform.athenahealth.com/v1/60768719/chart/encounter/60768719/orders/lab"






payload = 'diagnosissnomedcode=-19127489&facilityid=81592725&facilitynote=elit&futuresubmitdate=consectetur%20sunt%20laboris%20labore&highpriority=true&loinc=incididunt%20officia%20dolor&ordertypeid=18766226&providernote=proident%20ipsum%20pariatur'
headers = {
        'Authorization': 'qJZPU1Y69Oq3mkUovkabCcRXWpbC',
        'Content-Type': 'voluptate ad'
}

response = requests.request("POST", url, headers=headers, data=payload)

#print(response.text)
