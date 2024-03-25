"""
CAMY KAM
Assignment 1
CST8333 Programming Language Research Project
22W Semester
Language: Python
"""
import unittest
import DataInteraction_Persistence

"""Class to represent unittests involving adding incidents"""
class AddIncident(unittest.TestCase):
    """tests that a new record is added properly to a list"""
    def test_add_incident(self):
        new_incident="INC2022-001, Fire, 02/04/2022, Hearst, Ontario, CompanyX, Oil, Yes, Fire broke out at the center, Camy"
        method_incident=DataInteraction_Persistence.insert_new_record("INC2022-001", "Fire", "02/04/2022", "Hearst", "Ontario",
                                                                    "CompanyX", "Oil", "Yes", "Fire broke out at the center")             #CAMY KAM
        DataInteraction_Persistence.record_incidents.append(method_incident)

        self.assertEqual(new_incident,method_incident )
        self.assertIn(method_incident, DataInteraction_Persistence.record_incidents)              #CAMY KAM

if __name__ == '__main__':
    unittest.main()
