import unittest
import datetime

from app.constants import Constants as c
from app.input import Input, InputMonthly


class InputTest(unittest.TestCase):

    def testGetParamsDict_void_success(self):
        testclass = Input()
        params = testclass.get_params_dict()
        self.assertIsInstance(params, dict)


class InputMonthlyTest(unittest.TestCase):

    def setUp(self):
        self.testclass = InputMonthly()
        self.year = 2019
        self.month = 1

    def testGetDemandDict_wrongYear_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.get_demand_dict("hello", self.month)

    def testGetDemandDict_wrongMonth_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.get_demand_dict(self.year, "hello")

    def testGetDemandDict_wrongCurtail_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.get_demand_dict(self.year, self.month, "hello")

    def testGetDemandDict_correct_success(self):
        demand = self.testclass.get_demand_dict(self.year, self.month)
        self.assertIsInstance(demand, dict)
        for day, day_dict in demand.items():
            self.assertIsInstance(day, datetime.date)
            self.assertIsInstance(day_dict[c.WEEKDAY], int)
            for key, val in day_dict.items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(val, int)

    def testGetStaffDict_wrongYear_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.get_staff_dict("hello", self.month)

    def testGetStaffDict_wrongMonth_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.get_staff_dict(self.year, "hello")

    def testGetStaffDict_correct_success(self):
        staff = self.testclass.get_staff_dict(self.year, self.month)
        self.assertIsInstance(staff, dict)
        for name, values in staff.items():
            self.assertIsInstance(values, dict)
            self.assertIsInstance(name, str)
            self.assertIsInstance(values[c.WORKDAYS], int)
            self.assertIsInstance(values[c.JOBS], list)
            self.assertIsInstance(values[c.PRIO_JOB], str)
            self.assertIsInstance(values[c.WISHES], list)
            for wish in values[c.WISHES]:
                self.assertIsInstance(wish, dict)
                for date, prio in wish.items():
                    self.assertIsInstance(date, datetime.date)
                    self.assertTrue(prio in [c.PRIO1, c.PRIO2, c.PRIO3])


if __name__ == '__main__':
    unittest.main()
