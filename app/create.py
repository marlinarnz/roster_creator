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
        else:
            raise ValueError(e.WRONG_INPUT)
        if isinstance(output, Output):
            self._out = output
        else:
            raise ValueError(e.WRONG_OUTPUT)
        if isinstance(solver, Solver):
            self._solver = Solver
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
    staff's utility from free days and their dates under certain conditions.
    The multivariate solution algorithm under use is Nelder-Meat Simplex.'''

    def create(self, settings):
        ''' Creates the roster and passes the result to the output
        :param settings: dict with valid settings'''
        if self._check_settings(settings):
            year, month = self.__choose_timeframe(settings)
            # Create a roster in calendar format with demand data attributed
            self._roster = self._in.get_demand_dict(year, month, True)
            # Run the solver
            problem = self.__create_problem()
            result = self._solver.run(problem, self._roster)
            # Call the output
            self._out.generate(result, settings)
        else:
            raise ValueError(e.WRONG_SETTINGS)

    def __create_problem(self):
        return None

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
        pass

    def run(self, problem, roster_frame):
        raise NotImplementedError


class SolverSimplex(Solver):
    ''' A solver using the Nelder-Meat Simplex to find a solution for
    multivariate linear problems'''
    
    def run(self, problem, roster_frame):
        return roster_frame
