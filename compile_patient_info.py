# diagnosissnomedcode:-19127489 -- get the symptoms of the patient
# facilityid:81592725 -- get the home address of the  patient
# facilitynote:elit
# futuresubmitdate:2022-06-05 -- The date the order should be sent. Defaults to today.
# highpriority:true -- If true, then the order should be sent STAT. default = false.
# loinc:incididunt officia dolor -- The LOINC of the lab you wish to order.
# ordertypeid:18766226 -- The athena ID of the lab to order. Get the IDs using /reference/order/lab. Either this or
# LOINC can be used, but not both
# providernote -- will need to be spoken with the order. Default = empty


import pprint
import patient_info_call
from find_conditions_call import find_conditions
from patient_info_call import patient_info
import json
# athena's sample information:


def receive_order(input_string, patient_id, department_id, practice_id):
    # example: "order lipid panel"
    test_order = input_string[5:]
    priority = "default"
    if test_order.contains("stat"):
        priority = "STAT"
        test_order = test_order[0:len(test_order) - 4]
    compile_info(patient_id, practice_id, department_id, test_order, "today", priority)


def compile_info(patient_id, practice_id, department_id, test, futuresubmitdate, priority):
    #  TODO: Identify the lab LOINC or order type based on the string input
    patient_id = patient_id
    practice_id = practice_id
    department_id = department_id
    # patient_info1 = patient_info(practice_id, department_id, patient_id)
    patient_info = json.loads(patient_info_call.patient_info(practice_id, department_id, patient_id))
    patient_conditions = json.loads(find_conditions(practice_id, department_id, patient_id))
    #  get all activ1
    # conditions, and patient location.
    print(patient_info)
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
    # POST orders with given info


inputlist = []
message_array = ["Please enter a patient id", "Please enter a practice id", "Please enter a department id",
                 "What test will you be ordering?",
                 "Will it be submitted at a future date?", "What is the priority of your test?"]
for i in range(6):
    inputs = input(message_array[i])
    inputlist.append(inputs)

compile_info(inputlist[0], inputlist[1], inputlist[2], inputlist[3], inputlist[4], inputlist[5])
