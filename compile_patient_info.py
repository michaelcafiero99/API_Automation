# diagnosissnomedcode:-19127489 -- get the symptoms of the patient
# facilityid:81592725 -- get the home address of the  patient
# facilitynote:elit
# futuresubmitdate:2022-06-05 -- The date the order should be sent. Defaults to today.
# highpriority:true -- If true, then the order should be sent STAT. loinc:incididunt officia dolor
# loinc:incididunt officia dolor -- The LOINC of the lab you wish to order.
# ordertypeid:18766226 -- The athena ID of the lab to order. Get the IDs using /reference/order/lab. Either this or
# LOINC can be used, but not both.
# providernote -- will need to be spoken with the order. Default = empty
import pprint
from find_conditions_call import find_conditions
from patient_info_call import patient_info
import json

# athena's sample information:

patient_id = '0'
practice_id = '195900'
department_id = '1'
# patient_info1 = patient_info(practice_id, department_id, patient_id)
patient_info = json.loads(patient_info(practice_id, department_id, patient_id))
patient_conditions = json.loads(find_conditions(practice_id, department_id, patient_id))
#  get all active conditions, and patient location.

json1 = json.dumps((patient_info['entry']), sort_keys=True, indent=4)
dict2 = json.loads(json1)
address_info = (((dict2[0])['resource'])['address'])[0]
patient_city = address_info['city']
patient_country = address_info['country']
patient_line = address_info['line']
patient_zip = address_info['postalCode']
patient_state = address_info['state']

print("The patient lives at the address of " + patient_line[1] + ", " + patient_city + " "
      + patient_state + ", " + patient_country + ", " + patient_zip)
condition_dict = {}
for condition in patient_conditions['entry']:
    resource = condition['resource']
    status = resource['clinicalStatus']
    id = resource['id']
    code = resource['code']
    name = code['text']
    exists = False
    if name in condition_dict.values():
        exists = True

    if status == 'active' and not exists:
        condition_dict.update({id: name})
pp = pprint.PrettyPrinter(width=55, compact=True)
pp.pprint(condition_dict)
if len(condition_dict) > 20:
    print("Wow, this patient has a lot of problems! Notify the doctor that ordering tests won't be needed,"
          " they will be dead soon. ")


# print((patient_conditions['entry'][0]))

#  print(patient_conditions)
