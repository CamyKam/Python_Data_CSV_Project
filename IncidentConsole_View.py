"""
CAMY KAM
"""

import IncidentService_Business

menuOptions = {
    1: 'All Incidents',
    2: 'Search Incident',
    3: 'Create New Incident',
    4: 'Update Incident',
    5: 'Delete Incident',
    6: 'Save Incident Records to CSV',
    7: 'Exit Program'
}

searchIncidentOptions = {
    1: 'Incident Number',
    2: 'Province'
}

exit=False

def print_entire_list():
    """calls on the get_all_incidents method in the IncidentService_Business layer

    :return: the list of incidents
    """
    incidentList =IncidentService_Business.get_all_incidents()
    return incidentList

def search_incidents():
    """Asks users if they want to search by incident number or province and calls the related method accordingly"""

    print('What do you want to search by?')
    print_search_options()
    op =''
    try:
        op = int(input('Enter 1 or 2 '))
    except:
        print('Invalid input. Please enter a number ')
    if op == 1:
        incident_input= input('Enter the Incident Number: ')
        print(IncidentService_Business.get_searched_incident_number_record(incident_input))
        province_input = input ('Enter the province (capitalize First and Second word): ')
        IncidentService_Business.provinces_func(province_input)
        print(IncidentService_Business.get_searched_incident_by_province(province_input))
    else:
        print('Invalid Option Please Select Again')

def update_incident():
    """prompts user to enter details of the incident they wish to update and calls on the update_incident method

    :return: the result of calling the update_incident in the IncidentService_Business layer
    """
    incident_number= input('Which incident did you want to update/edit? (Enter the exact incident number): ')
    print('----Here is the incident you are updating----')
    incident=IncidentService_Business.get_searched_incident_number_record(incident_number)
    if incident=='Could not find this incident in records':
        return print('Cannot Update, could not find incident in records')
    incident_type = input ('Enter the incident type: ')
    reported_date = input ('Enter the reported date (follow format \'mm/dd/yyyy\': ')
    nearest_center = input ('Enter the nearest populated center: ')
    province = input ('Enter the province the incident occurred in: ')
    company = input ('Enter the associated company: ')
    substance = input ('Enter the substance involved: ')
    significant = input ('Was the incident significant? (Type Yes or No): ')
    whatHappened = input ('Describe what happened: ')

    return IncidentService_Business.update_incident(incident_number, incident_type, reported_date, nearest_center, province, company, substance, significant, whatHappened)

def print_menu():
    """displays the menu options to the user for this program"""

    for options in menuOptions.keys():
        print (options, '>', menuOptions[options])

def print_search_options():
    """displays the search options for incidents """
    for options in searchIncidentOptions.keys():
        print(options, '>', searchIncidentOptions[options])

def view_all_incidents():
    """calls the print_entire_list method"""

    print_entire_list()

def delete_incident():
    """ prompts user to enter an incident they wish to delete and calls the delete_incident method"""

    incident_num= input('Enter the incident number you wish to delete: ')
    IncidentService_Business.delete_incident(incident_num)

def create_incident():
    """Prompts user to provide information for creating a new incident and calls the insert_incident method

    :return: the result of calling the insert_incident method
    """
    print('Enter information about the incident by following the prompts below one by one')
    incidentNum= str(input('Enter Incident Number (Follow format \'INCXXXX-YYY\' where X is the year ' 
                           'and Y is a number for that year: '))
    incidentType= str(input('Enter the Incident Type: '))
    reportedDate = str(input('Enter the reported date (follow format \'mm/dd/yyyy\': '))
    nearestCenter = str(input('Enter the nearest populated center at the time: '))
    province = str(input('Enter the province it occured in: '))
    company = str(input('Enter the company associated with it: '))
    substance = str(input('Enter the substance involved: '))
    significant = str(input('Was it significant? (Yes or No): '))
    whatHappened = str(input('Explain what happened: '))

    return IncidentService_Business.insert_incident(incidentNum, incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened)

def save_data_to_csv():
    """calls the save_data_as_csv method from the IncidentService_Business layer"""

    IncidentService_Business.save_data_as_csv()

while(exit != True):
    print("\r")
    print("Program Designed by Camy Kam")
    print_menu()
    option = ''
    try:
        option = int(input('Select Your Choice of Action: '))
    except:
        print('Wrong input. Please enter a number ...')

    if option == 1:
        view_all_incidents()
    elif option == 2:
        search_incidents()
    elif option == 3:
        create_incident()
    elif option == 4:
        update_incident()
    elif option == 5:
        delete_incident()
    elif option == 6:
        save_data_to_csv()
    elif option == 7:
        print('You have exited the program')
        exit = True
    else:
        print('Invalid option. Please enter a number option between 1 and 4.')


