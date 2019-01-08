import datetime

from app.constants import Constants as c
from app.input import InputMonthly
from app.output import OutputFactory
from app.create import CreatorUtility, SolverSimplex


inp = InputMonthly()
out = OutputFactory()
solv = SolverSimplex()
creator = CreatorUtility(inp, out, solv)
settings = {c.START: datetime.date(2019, 1, 1),
            c.END: datetime.date(2019, 31, 1),
            c.EXCEL_OUT: True}
creator.create(settings)
