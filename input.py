import datetime

import Constants as c


class InputReader:
    """ This class contains all methods necessary to read all information into the staff roster"""

    def __init__(self):
        pass
 
    def get_data(self):
        staff_dict = {"Marlin": {c.WORKDAYS: 4,
                                 c.CLASSES: ["Saisonnier m"],
                                 c.PRIO_CLASS: "Saisonnier m",
                                 c.WISHES: [{datetime.datetime(2019, 01, 02): c.PRIO3}]}
                     }
        slots = get_calender_dict(datetime.datetime.today().year(),
                                  datetime.datetime.today().month() + 1)

    def get_calendar_dict(self, year, month):
        pass
