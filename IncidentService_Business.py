"""
CAMY KAM
"""

import DataInteraction_Persistence
from enum import Enum

list =[]

class Provinces(Enum):
    """An enum class containing the list of all Canadian provinces and territories"""

    Ontario ="Ontario"
    Alberta ="Alberta"
    British_Columbia= "British Columbia"
    Manitoba= "Manitoba"
    New_Brunswick ="New Brunswick"
    Newfoundland_and_Labrador="Newfoundland and Labrador"
    Northwest_Territories = "Northwest Territories"
    Nova_Scotia ="Nova Scotia"
    Nunavut= "Nunavut"
    Prince_Edward_Island= "Prince Edward Island"
    Quebec = "Quebec"
    Saskatchewan="Saskatchewan"
    Yukon="Yukon"

def provinces_func(input_province):
    """checks if the user entered province is a valid province

    :param input_province: User provided province name
    :return: 'Fail' if the province was unable to be located from the Provinces class
    """
    provinces_list=[]
    for choice in Provinces:
        provinces_list.append(choice.value)

    if input_province not in provinces_list:
        return ('Fail')

def get_all_incidents():
    """calls the get_all_records method in the DataInteraction_Persistence layer
    :return: the list result from calling the get_all_records method
    """
    list = DataInteraction_Persistence.get_all_records()
    return list

def insert_incident(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened):
    """calls the insert_new_record method in the DataInteraction_Persistence layer

    :param incidentNum: the incident number
    :param incidentType: what type of incident it was
    :param reportedDate: date that the incident was reported
    :param nearestCenter: the nearest populated center to the incident
    :param province:province in Canada where the incident occurred
    :param company: the company that owns or operates the facility or pipeline where the incident occurred
    :param substance: substance that was released
    :param significant: whether incident was a significant one
    :param whatHappened: what occurred with the pipeline
    :return: printed string that the inserted incident was added
    """
    list = DataInteraction_Persistence.insert_new_record(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened)
    return print('Incident was added')

def get_searched_incident_number_record(incidentNum):
    """calls the get_record_by_incident_num method in the DataInteraction_Persistence layer

    :param incidentNum: the incident number
    :return: either a string message that results were found or that they were not found
    """
    incident=DataInteraction_Persistence.get_record_by_incident_num(incidentNum)
    if incident== False:
        return str('Could not find this incident in records')
    return str('Results Found')

def get_searched_incident_by_province(province):
    """calls the get_records_by_province method in the DataInteraction_Persistence layer

    :param province: province in Canada where the incident occurred
    :return: either a string message that results were found or that the province could not be found/invalid
    """
    verification_results=provinces_func(province)
    if verification_results=='Fail':
        return str('Invalid province please try again')
    province_incident=DataInteraction_Persistence.get_records_by_province(province)
    if province_incident== False:
        return str('Could not find a province with this name')
    return str('Results Found')

def update_incident(incident_number, incident_type, reported_date, nearest_center, province, company, substance, significant, whatHappened):
    """calls the update_record method in the DataInteraction_Persistence layer

    :param incidentNum: the incident number
    :param incidentType: what type of incident it was
    :param reportedDate: date that the incident was reported
    :param nearestCenter: the nearest populated center to the incident
    :param province:province in Canada where the incident occurred
    :param company: the company that owns or operates the facility or pipeline where the incident occurred
    :param substance: substance that was released
    :param significant: whether incident was a significant one
    :param whatHappened: what occurred with the pipeline
    :return: the result of calling the update_record method
    """
    return DataInteraction_Persistence.update_record(incident_number, incident_type, reported_date, nearest_center, province, company, substance, significant, whatHappened)

def delete_incident(incident_number):
    """calls the delete_record method in the DataInteraction_Persistence layer

    :param incident_number: the incident number
    :return: the result of calling the delete_record method
    """
    return DataInteraction_Persistence.delete_record(incident_number)

def save_data_as_csv():
    """calls the write_to_csv method in the DataInteraction_Persistence layer
    :return: the result of calling the write_to_csv method
    """
    return DataInteraction_Persistence.write_to_csv()