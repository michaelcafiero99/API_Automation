import requests
import json
from token_call import get_token


# TODO: Ability to modify the url based on the patient, and practice
def find_conditions(practice_id, department_id, patient_id):
    url = "https://api.preview.platform.athenahealth.com/v1/195900/1/fhir/dstu2/Condition?patient=1" \
          "&THIRDPARTYUSERNAME=in " \
          "eu&PATIENTFACINGCALL=true "
    auth_string = get_token()
    payload = {}
    headers = {
        'Accept': 'application/json',
        'practiceid': practice_id,
        'Authorization': auth_string
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    json_object = json.loads(response.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    #print(json_formatted_str)
    return json_formatted_str
