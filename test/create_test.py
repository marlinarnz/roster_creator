import unittest
import datetime

from app.constants import Constants as c
from app.create import Creator, CreatorUtility, Solver, SolverSimplex
from app.input import Input
from app.output import Output


class CreatorTest(unittest.TestCase):

    def setUp(self):
        self.input = Input()
        self.output = Output()
        self.solver = Solver()
        self.testclass = Creator(self.input, self.output)
        self.settings = {c.START: datetime.date.today(),
                         c.END: datetime.date(2019, 1, 31)}

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
        self.settings["hello"] = 22344
        with self.assertRaises(ValueError):
            self.testclass.create(self.settings)

    def testCreate_correct_exception(self):
        with self.assertRaises(NotImplementedError):
            self.testclass.create(self.settings)
