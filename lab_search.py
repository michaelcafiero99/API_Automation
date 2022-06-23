import requests
import json
from maps_api import find_directions
import pprint
pp = pprint.PrettyPrinter(indent=3)


def lab_search(address, zipcode):
    # with real patient data, the address will be the patient address obtained in compile_patient_info
    zipcode = '05403'
    address = 'STONEHEDGE DRIVE, SOUTH BURLINGTON VT, 05403'
    url = "https://clia-lab-search.p.rapidapi.com/api/labs"

    querystring = {"zip_code": zipcode}

    headers = {
        "X-RapidAPI-Key": "AIzaSyDcIFrPGVaKYimsmEA3Lk69kBoqHJO92Qw",
        "X-RapidAPI-Host": "clia-lab-search.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    json_object = json.loads(response.text)
    json_formatted_str = json.dumps(json_object, indent=2)
    # return only "Ancillary Test Sites"
    #  get all active conditions, and patient location.
    testing_list = []
    dict_list = json.loads(json_formatted_str)

    for dict in dict_list:
        facility_type = dict['general_facility_type']
        if facility_type == "Ancillary Test Site" or facility_type == "Hospital"  or facility_type == "Mobile Lab":
            address = dict['address'] + ", " + dict['city_name'] + " " + dict['state_code'] + ", " + dict['zip_code']
            testing_list.append(address)

    pp.pprint(testing_list)

    for testing_site in testing_list:
        find_directions(address, testing_site)

lab_search('STONEHEDGE DRIVE, SOUTH BURLINGTON VT, 05403', '05403')
