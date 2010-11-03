"""
Example cronjob:

from cronjobs.base import Cron
from cronjobs.constants import MINUTES
from mailchimp.utils import dequeue

class DequeueCron(Cron):
    run_every = 1
    interval_unit = MINUTES
 
    def job(self):
        try:
            dequeue()
            return True
        except:
            return False
"""