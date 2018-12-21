class Constants:
    ''' The constants class contains all necessary constant numbers, dictionary keys and suchlike'''

    PARAMS = "params.json"
    # Keys for the params.json file
    JOBS = "jobs"
    UT = "utility"
    UT_OFF_ROW = "off_in_row"
    UT_OFF_PRIO1 = "off_prio1"
    UT_OFF_PRIO2 = "off_prio2"
    UT_OFF_PRIO3 = "off_prio3"
    
    # Keys for the calendar dict
    WEEKDAY = "weekday"
    
    # Keys for the staff dict
    WORKDAYS = "working days per week"
    PRIO_JOB = "prioritized job"
    WISHES = "day off wiches list"
    PRIO1 = "day off priority 1"
    PRIO2 = "day off priority 2"
    PRIO3 = "day off priority 3"

class Errors:
    ''' This class contains error messages '''

    WRONG_INPUT = "An instance of the Input class is needed for instanciation of the creator"
    WRONG_OUTPUT = "An instance of the Output class is needed for instanciation of the creator"
