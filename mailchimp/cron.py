from cronjobs.base import Cron
from mailchimp.utils import dequeue

class DequeueCron(Cron):
    run_every = 30 # run every 30 seconds
 
    def job(self):
        try:
            dequeue()
            return True
        except:
            return False