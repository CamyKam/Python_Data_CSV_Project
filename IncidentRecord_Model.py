"""
CAMY KAM
"""

class Incident:
    """ A class to represent a pipeline incident

    Attributes
    -----------
    incidentNum : str
        the incident number
    incidentType: str
        what type of incident it was
    reportedDate : str
        date that the incident was reported
    nearestCenter : str
        the nearest populated center to the incident
    province : str
        province in Canada where the incident occurred
    company : str
        the company that owns or operates the facility or pipeline where the incident occurred
    substance : str
        substance that was released
    significant : str
        whether incident was a significant one
    whatHappened : str
        what occurred with the pipeline

    """
    def __init__(self, incidentNum,incidentType, reportedDate, nearestCenter, province, company, substance, significant, whatHappened):
        """Constructs an Incident Object

        :param incidentNum: the incident number
        :param incidentType: what type of incident it was
        :param reportedDate: date that the incident was reported
        :param nearestCenter: the nearest populated center to the incident
        :param province:province in Canada where the incident occurred
        :param company: the company that owns or operates the facility or pipeline where the incident occurred
        :param substance: substance that was released
        :param significant: whether incident was a significant one
        :param whatHappened: what occurred with the pipeline
        """
        self.incidentNum = incidentNum
        self.incidentType= incidentType
        self.reportedDate = reportedDate
        self.nearestCenter = nearestCenter
        self.province = province
        self.company = company
        self.substance = substance
        self.significant = significant
        self.whatHappened = whatHappened



    def __str__(self):
        """Prints the various attributes related to the Incident Object

        :return: Incident object attributes in a string format
        """
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s,'%(self.incidentNum, self.incidentType,self.reportedDate,self.nearestCenter, self.province, self.company,
                              self.substance,self.significant, self.whatHappened )


