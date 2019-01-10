import unittest
import datetime

from app.constants import Constants as c
from app.create import Creator, CreatorUtility, Solver, SolverMIP
from app.input import Input, InputMonthly
from app.output import Output

SETTINGS = {c.START: datetime.date.today(),
            c.END: datetime.date(2019, 1, 31),
            c.EXCEL_OUT: True}


class CreatorTest(unittest.TestCase):

    def setUp(self):
        self.input = Input()
        self.output = Output()
        self.solver = Solver()
        self.testclass = Creator(self.input, self.output)

    def testInit_wrongInput_exception(self):
        with self.assertRaises(ValueError):
            testclass = Creator("hello", self.output, self.solver)

    def testInit_wrongOutput_exception(self):
        with self.assertRaises(ValueError):
            testclass = Creator(self.input, "hello", self.solver)

    def testInit_wrongSolver_exception(self):
        with self.assertRaises(ValueError):
            testclass = Creator(self.input, self.output, "hello")

    def testInit_correct_success(self):
        testclass = Creator(self.input, self.output, self.solver)
        self.assertTrue(True)

    def testCreate_wrongSettingsKey_exception(self):
        settings = SETTINGS
        settings["hello"] = 22344
        with self.assertRaises(ValueError):
            self.testclass.create(SETTINGS)

    def testCreate_correct_exception(self):
        with self.assertRaises(NotImplementedError):
            self.testclass.create(SETTINGS)


class SolverTest(unittest.TestCase):

    def testInit_void_void(self):
        solver = Solver()

    def testRun_correct_exception(self):
        with self.assertRaises(NotImplementedError):
            solver = Solver()
            solver.run()


class SolverMIPTest(unittest.TestCase):

    def setUp(self):
        self.testclass = SolverMIP()
        self.input_monthly = InputMonthly()
        self.month = 1
        self.year = 2019
        self.roster_month = self.input_monthly.get_demand_dict(self.year, self.month, True)
        self.roster_full_weeks = self.input_monthly.get_demand_dict(self.year, self.month, False)
        self.staff = self.input_monthly.get_staff_dict(self.year, self.month)

    def testRun_wrongRoster_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.run("hello", self.staff)

    def testRun_wrongStaff_exception(self):
        with self.assertRaises(ValueError):
            self.testclass.run(self.roster_month, "hello")

    def testRun_rosterMonth_success(self):
        # TODO
        pass

    def testRun_rosterFullWeeks_success(self):
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()
