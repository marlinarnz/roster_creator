
import datetime
import calendar
import json

from app.constants import Constants as c
from app.dataclasses import Staff


class Input:
    ''' This class contains all methods necessary to read all information into
    the staff roster'''

    def __init__(self):
        self._params = json.load(open(c.PARAMS))

    def get_params_dict(self):
        return self._params


class InputMonthly(Input):
    ''' This class returns monthly input data for creation of a staff roster'''

    def get_demand_dict(self, year, month, curtail=True):
        ''' This method returns the demand for staff in the given month
        to calculate the staff roster.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :param curtail: bool whether to cut off all weekdays from
        the calendar that do not belong to the given month
        (optional, default true)
        :return dict with days and their need for staff roles'''

        calendar_dict = self.__get_calendar_dict(year, month, curtail)

        # Attribute default staff demand from params
        for job, demand in self._params[c.JOBS].items():
            for day, day_dict in calendar_dict.items():
                day_dict[job] = demand

        # Alter the staff demand
        # TODO

        return calendar_dict

    def get_staff_list(self, year, month):
        ''' This method returns the staff data to calculate the roster.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :return list with staff object instances'''

        staff_list = [Staff(name="Marlin", workdays=4, 
                            jobs=["Saisonnier m"],
                            wishes={datetime.date(2019, 1, 2): c.PRIO3},
                            prio_job="Saisonnier m")
                     ]
        return staff_list

    def __get_calendar_dict(self, year, month, curtail=True):
        ''' This method uses the calendar package to iterate over
        one given month's days and return them in a dictionary
        with each day being another dictionary with weekday.
        :param year: int giving a year within 1700 and 2100
        :param month: int giving a month within 1 (Jan) and 12 (Dec)
        :param curtail: bool whether to cut off all weekdays from
        the calendar that do not belong to the given month
        (optional, default true)'''

        month_dict = {}
        cal = calendar.Calendar()
        for day in cal.itermonthdates(year, month):
            if day.month == month or not curtail:
                month_dict[day] = {c.WEEKDAY: day.weekday()}
        return month_dict
