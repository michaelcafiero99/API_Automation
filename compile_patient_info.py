# diagnosissnomedcode:-19127489 -- get the symptoms of the patient
# facilityid:81592725 -- get the home address of the  patient
# facilitynote:elit
# futuresubmitdate:2022-06-05 -- The date the order should be sent. Defaults to today.
# highpriority:true -- If true, then the order should be sent STAT. loinc:incididunt officia dolor
# loinc:incididunt officia dolor -- The LOINC of the lab you wish to order.
# ordertypeid:18766226 -- The athena ID of the lab to order. Get the IDs using /reference/order/lab. Either this or
# LOINC can be used, but not both.
# providernote -- will need to be spoken with the order. Default = empty

from find_conditions_call import find_conditions
from patient_info_call import patient_info
# athena's sample information:
patient_id = '1'
practice_id = '195900'
department_id = '1'

patient_info = patient_info(practice_id, department_id, patient_id)
patient_conditions = find_conditions(practice_id, department_id, patient_id)
print(patient_info)
print(patient_conditions)
