import json

# from scipy.optimize import linprog, fmin_bfgs
# from numpy import array, matrix

from app.constants import Constants as c
from app.constants import Errors as e
from app.input import Input
from app.output import Output


class Creator:
    '''Interface'''

    def __init__(self, input, output, solver):
        ''' Constructor
        :param input: Input class instance to retrieve the demand and supply
        of staff
        :param output: Output class instance to output the results
        :param solver: Solver class instant as algorithm under use'''
        if isinstance(input, Input):
            self._in = input
            self._roster = None
            self._staff = None
        else:
            raise ValueError(e.WRONG_INPUT)
        if isinstance(output, Output):
            self._out = output
        else:
            raise ValueError(e.WRONG_OUTPUT)
        if isinstance(solver, Solver):
            self._solver = solver
        else:
            raise ValueError(e.WRONG_SOLVER)

    def create(self, settings):
        if self._check_settings(settings):
            raise NotImplementedError
        else:
            raise ValueError(e.WRONG_SETTINGS)

    def _check_settings(self, settings):
        if isinstance(settings, dict):
            if len(settings.keys()) == len(c.SETTINGS_KEYS):
                for key, val in settings.items():
                    if key in c.SETTINGS_KEYS:
                        return True
        return False


class CreatorUtility(Creator):
    ''' This class creates a staff roster based on optimization of the
    staff's utility from free days and their dates under certain conditions.'''

    def create(self, settings):
        ''' Creates the roster and passes the result to the output
        :param settings: dict with valid settings'''
        if self._check_settings(settings):
            year, month = self.__choose_timeframe(settings)
            # Get the input data
            self._roster = self._in.get_demand_dict(year, month, True)
            self._staff = self._in.get_staff_list(year, month)
            # Run the solver
            result = self._solver.run(self._roster, self._staff)
            # Call the output
            self._out.generate(result, settings)
        else:
            raise ValueError(e.WRONG_SETTINGS)

    def __choose_timeframe(self, settings):
        ''' Method to calculate the timeframe from start and end date of the
        settings
        :param settings: dict with start and end dates in date format
        :return year, month: int'''
        # TODO: something smarter
        year = settings[c.END].year
        month = settings[c.END].month
        return year, month


class Solver:
    ''' Interface'''

    def __init__(self):
        self._params = json.load(open(c.PARAMS))

    def run(self):
        raise NotImplementedError


class SolverMIP(Solver):
    ''' A solver based on non-linear utility maximization. A mixed integer
    problem (MIP) is constructed.'''

    def run(self, roster_frame, staff_list):
        '''
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog
        https://stackoverflow.com/questions/26305704/python-mixed-integer-linear-programming
        solver packages
        https://github.com/SCIP-Interfaces/PySCIPOpt
        https://github.com/SCIP-Interfaces/PySCIPOpt/blob/master/examples/finished/sudoku.py
        http://cvxopt.org/documentation/index.html
        http://www.mipcl-cpp.appspot.com/static/docs/mipcl-py/html/index.html
        https://www.gnu.org/software/glpk/
        '''
        from PySCIPOpt import Model
        model = Model()
        off = [[model.addVar(name=staff.name + "_" + str(day),
                             vtype="B", obj=0)
                 for day, val in roster_frame.items()]
                for staff in staff_list]
        ut_wishes = [[self._params[c.UT][c.PRIO_MAP[v[c.WISHES][day]]]
                      for staff in staff_list
                      if day in staff.wishes.keys() else 0]
                     for day, val in roster_frame.items()]
        model.setObjective()

        return roster_frame
