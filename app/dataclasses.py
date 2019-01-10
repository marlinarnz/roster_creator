from app.constants import Errors as e

class Staff:
    ''' Object representing a staff member with roles, wishes and other specs'''

    def __init__(self, name, workdays, jobs, wishes, prio_job=None):
        ''' Constructor
        :param name: String giving the name of the person
        :param workdays: int defining the working days per week (7 days)
        :param jobs: list of jobs that can be attended
        :param wishes: dict with date objects as keys and a priorities as values
        :param prio_job: job where this person is prioritized'''
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError(e.WRONG_STAFF_NAME)
        if isinstance(workdays, int):
            self.workdays = workdays
        else:
            raise ValueError(e.WRONG_STAFF_WORKDAYS)
        if isinstance(jobs, list):
            self.jobs = jobs
        else:
            raise ValueError(e.WRONG_STAFF_JOBS)
        if isinstance(wishes, int):
            self.wishes = wishes
        else:
            raise ValueError(e.WRONG_STAFF_WISHES)
        if prio_job is not None:
            if isinstance(prio_job, str) and prio_job in self.wishes:
                self.prio_job = prio_job
            else:
                raise ValueError(e.WRONG_STAFF_PRIO_JOB)
