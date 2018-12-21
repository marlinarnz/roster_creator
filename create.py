import Constants as c
import Errors as e
from input import Input
from output import Output


class Creator:

    def __init__(self, input, output):
        ''' Constructor
        :param input: Input class instance to retrieve the demand and supply of staff
        :param output: Output class instance to output the results'''
        if isinstance(input, Input):
            self.__in = input
        else:
            raise TypeError(e.WRONG_INPUT)
        if isinstance(output, Output):
            self.__out = output
        else:
            raise TypeError(e.WRONG_OUTPUT)


class CreatorUtility(Creator):
    pass
