import datetime
import calendar
import json

import Constants as c


class InputReader:
    """ This class contains all methods necessary to read all information into the staff roster"""

    def __init__(self):
        self.__params = json.load(open(c.JSON))
 
    def get_data(self, year, month, curtail=True):
        ''' This method returns all necessary data to calculate the
        staff roster.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :param curtail: bool whether to cut off all weekdays from
        the calendar that do not belong to the given month
        (optional, default true)
        :return staff_dict: dict with staff members and their specs
        :return need_dict: dict with days and their need for staff roles'''

        staff_dict = {"Marlin": {c.WORKDAYS: 4,
                                 c.CLASSES: ["Saisonnier m"],
                                 c.PRIO_CLASS: "Saisonnier m",
                                 c.WISHES: [{datetime.date(2019, 1, 2): c.PRIO3}]}
                     }
        need_dict = get_staff_need_dict(year, month, curtail)
        return staff_dict, need_dict

    def get_staff_need_dict(self, year, month, curtail=True):
        ''' This method returns the number of necessary staff for
        each job at each day.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :param curtail: bool whether to cut off all weekdays from
        the calendar that do not belong to the given month
        (optional, default true)'''
        
        staff_need_dict = get_calendar_dict(year, month, curtail)
        for job in self.__params[c.JOBS]:
            for day, val in staff_need_dict.items():
                val[job] = self.__params[job]
        return staff_need_dict

    def get_calendar_dict(self, year, month, curtail=True):
        ''' This method uses the calendar package to iterate over
        one given month's days and return them in a dictionary
        with each day being another dictionary with weekday.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :param curtail: bool whether to cut off all weekdays from
        the calendar that do not belong to the given month
        (optional, default true)'''

        month_dict = {}
        cal = canledar.Calendar()
        for day in cal.itermonthdates(year, month):
            if day.month == month or not curtail:
                month_dict[day] = {c.WEEKDAY: day.weekday()}
        return month_dict
