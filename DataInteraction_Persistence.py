"""
CAMY KAM
"""

import pandas as pd;
import numpy as np;
from IncidentRecord_Model import Incident;

data_columns=['Incident Number', 'Incident Types', 'Reported Date', 'Nearest Populated Centre', 'Province', 'Company',
         'Substance', 'Significant', 'What happened category']
date_column_headers= "Incident Number, Incident Types, Reported Date, Nearest Populated Centre, Province, Company, " \
                    "Substance, Significant, What happened category"
csv_file= 'pipeline-incidents-comprehensive-data.csv'
new_csv_file='new-pipeline-incidents-data.csv'
global record_incidents
record_incidents=[]

def get_all_records():
    """prints all the records in the data structure """
    load_current_records()
    print_list(record_incidents)

def insert_new_record(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened):
    """calls create_incident_object method to create a new Incident object and appends it to the list of record_incidents

    :param incidentNum: the incident number
    :param incidentType: what type of incident it was
    :param reportedDate: date that the incident was reported
    :param nearestCenter: the nearest populated center to the incident
    :param province:province in Canada where the incident occurred
    :param company: the company that owns or operates the facility or pipeline where the incident occurred
    :param substance: substance that was released
    :param significant: whether incident was a significant one
    :param whatHappened: what occurred with the pipeline
    :return: the new object created as a string
    """
    new_Incident_Obj= create_incident_bbject(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened)

    load_current_records()
    record_incidents.append(new_Incident_Obj)

    return new_Incident_Obj.__str__()

def get_record_by_incident_num(providedIncidentNum):
    """searches for the user provided incident number in current records

    :param providedIncidentNum: User provided number of the incident
    :return: called method print_list to print the incident found or returns False if no records found
    """
    load_current_records()
    filtered_list = [i for i in record_incidents if i.incidentNum == providedIncidentNum]
    incident_num_list = []

    if filtered_list:
        for incident in filtered_list:
            incident_num_list.append([incident.incidentNum, incident.incidentType, incident.reportedDate, incident.nearestCenter, incident.province,
                                    incident.company, incident.substance, incident.significant, incident.whatHappened])

        filtered_list.clear()
        return print_list(incident_num_list)
    else:
        filtered_list.clear()
        return False

def get_records_by_province(providedProvince):
    """searches for all records where the province in an incident matches the user provided province

    :param providedProvince: Canadian province provided by user input
    :return: called method print_list to print all incidents found or returns false if there are no results found
    """
    load_current_records()
    filter_list = [i for i in record_incidents if i.province == providedProvince]
    province_list= []

    if filter_list:
        for incident in filter_list:
            province_list.append([incident.incidentNum, incident.incidentType, incident.reportedDate, incident.nearestCenter, incident.province,
                                    incident.company, incident.substance, incident.significant, incident.whatHappened])

        filter_list.clear()
        return print_list(province_list)
    else:
        filter_list.clear()
        return False

def update_record(incident_number, incident_type, reported_date, nearest_center, province, company, substance, significant, whatHappened):
    """updates an existing record in the record incidents list with new user provided values

    :param incidentNum: the incident number
    :param incidentType: what type of incident it was
    :param reportedDate: date that the incident was reported
    :param nearestCenter: the nearest populated center to the incident
    :param province:province in Canada where the incident occurred
    :param company: the company that owns or operates the facility or pipeline where the incident occurred
    :param substance: substance that was released
    :param significant: whether incident was a significant one
    :param whatHappened: what occurred with the pipeline
    :return: printed message of the incident number and its updated values or a message if the incident could not be found
    """
    load_current_records()
    found = False

    for incident in record_incidents:
        if incident.incidentNum == incident_number:
            found= True
            record_index_value = record_incidents.index(incident)

    if found == False:
        return ('This record cannot be found and updated')

    record_incidents[record_index_value] = create_incident_bbject(incident_number, incident_type, reported_date, nearest_center, province, company, substance, significant, whatHappened)
    updated_record = record_incidents[record_index_value]

    return print('Updated incident ', incident_number, 'to the following information: ', updated_record )

def delete_record(incident_number):
    """deletes a record from the record_incidents list

    :param incident_number:the incident number
    :return: print message indicating the incident number deleted or a message that the record could not be found if it doesn't exist
    """
    load_current_records()
    found = False

    for incident in record_incidents:
        if incident.incidentNum == incident_number:
            found = True
            record_index_value = record_incidents.index(incident)

    if found == False:
        return print('This record cannot be found and deleted')

    try:
        del record_incidents[record_index_value]
    except:
        return ('Unable to delete the record')

    return print('Deleted incident ', incident_number, 'from the list of incidents')

def load_current_records():
    """calls on the load_file_records method if the record_incidents list is empty"""
    if not record_incidents:
        load_file_records()

def create_incident_bbject(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened):
    """Creates an object of the Incident Class

    :param incidentNum: the incident number
    :param incidentType: what type of incident it was
    :param reportedDate: date that the incident was reported
    :param nearestCenter: the nearest populated center to the incident
    :param province:province in Canada where the incident occurred
    :param company: the company that owns or operates the facility or pipeline where the incident occurred
    :param substance: substance that was released
    :param significant: whether incident was a significant one
    :param whatHappened: what occurred with the pipeline
    :return: a new object of the Incident Class
    """
    incident_obj= Incident(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened)
    return incident_obj

def print_list(list):
    """ prints out each object in a list
    :param list: a list
    """
    for object in list:
        print(object)

def load_file_records():
    """reads through a csv and loads all data from the file to append to the record_incidents list

    :return: the record_incidents list
    """
    try:
        df = pd.read_csv(csv_file, encoding='latin-1', usecols=data_columns)
    except IOError as error:
        print(error)

    for i in range(100):
        try:
            incidentNum= df["Incident Number"][i]
            incidentType= df["Incident Types"][i]
            reportedDate = df["Reported Date"][i]
            nearestCenter= df["Nearest Populated Centre"][i]
            province= df["Province"][i]
            company= df["Company"][i]
            substance= df["Substance"][i]
            significant= df["Significant"][i]
            whatHappened= df["What happened category"][i]
        except KeyError as ke:
            print(ke, "Please review this column name again to ensure it's correct or exists")

        try:
            new_incident= create_incident_bbject(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened)
        except NameError as ne:
            print(ne, 'Ensure that the argument is correct')
            break
        except TypeError as te:
            print(te, 'Argument(s) are missing, please check that the correct names and number are present')
            break

        record_incidents.append(new_incident)
    return record_incidents

def write_to_csv():
    """takes the elements from the record_incidents list and writes the data into a csv file

    :return:either a message indicating that a new csv file has been created or if there was an issue
    """
    if not record_incidents:
        try:
            df = pd.read_csv(csv_file, encoding='latin-1', usecols=data_columns)
        except IOError as error:
            print(error)

        for i in range(100):
            try:
                incidentNum = df["Incident Number"][i]
                incidentType = df["Incident Types"][i]
                reportedDate = df["Reported Date"][i]
                nearestCenter = df["Nearest Populated Centre"][i]
                province = df["Province"][i]
                company = df["Company"][i]
                substance = df["Substance"][i]
                significant = df["Significant"][i]
                whatHappened = df["What happened category"][i]
            except KeyError as ke:
                print(ke, "Please review this column name again to ensure it's correct or exists")

            try:
                new_incident = create_incident_bbject(incidentNum, incidentType, reportedDate, nearestCenter, province,
                                                      company, substance, significant, whatHappened)
            except NameError as ne:
                print(ne, 'Ensure that the argument is correct')
                break
            except TypeError as te:
                print(te,
                      'Argument(s) are missing, please check that the correct names and number are present')
                break

            record_incidents.append(new_incident.__str__())

    numpy_array = np.array(record_incidents)
    try:
        np.savetxt(new_csv_file, numpy_array, '%s', delimiter=",", header=date_column_headers)
    except:
        return('An issue has occured with saving the text to csv')

    return print('A new incident data csv file has been created')




