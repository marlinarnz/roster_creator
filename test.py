import unittest
from test.input_test import InputTest, InputMonthlyTest
from test.create_test import CreatorTest


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(InputTest))
    suite.addTests(unittest.makeSuite(InputMonthlyTest))
    suite.addTests(unittest.makeSuite(CreatorTest))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
