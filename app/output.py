import json
import pandas as pd

from app.constants import Constants as c
from app.constants import Errors as e


class Output:
	''' Interface'''

	def __init__(self):
		self._params = json.load(open(c.PARAMS))

	def generate(result, settings):
		if self._check_settings(settings):
			self._create(result, settings)
		else:
			raise ValueError(e.WRONG_SETTINGS)

	def _create(self, result, settings):
		raise NotImplementedError

	def _check_settings(self, settings):
		if isinstance(settings, dict):
			if len(settings.keys()) == len(c.SETTINGS_KEYS):
				for key, val in settings.items():
					if key in c.SETTINGS_KEYS:
						return True
		return False


class OutputFactory(Output):
	''' Factory class which calls the wanted outputs'''

	def _create(self, result, settings):
		excel = OutputExcel()
		excel.generate(result, settings)


class OutputExcel(Output):
	''' Class to generate an Excel output'''

	def _create(self, result, settings):
		''' Creates an Excel worksheet structured in a similar way as the old
		one.
		:param result: dict with keys being dates in date format
		:param settings: dict with valid settings'''
		writer = pd.ExcelWriter(self._params[c.PATH_OUT] +
								settings[c.NAME_OUT] +
								self._params[c.EXCEL_EXTENSION])
		df = pd.DataFrame()
		# TODO
