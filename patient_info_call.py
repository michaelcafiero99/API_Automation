import requests
import requests.auth
import json
from token_call import get_token


def patient_info(practice_id, department_id, patient_id):
    url = "https://api.preview.platform.athenahealth.com/v1/195900/1/fhir/dstu2/Patient?given=exercitation " \
          "aliq&identifier=exercitation aliq&_id=1&birthdate=exercitation aliq&name=exercitation aliq&family=exercitation " \
          "aliq&gender=exercitation aliq&THIRDPARTYUSERNAME=exercitation aliq&PATIENTFACINGCALL=true "
    auth_string = get_token()
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': auth_string
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    #  print(json_formatted_str)
    return json_formatted_str
