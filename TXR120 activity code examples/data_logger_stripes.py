from ev3dev.auto import *
from time import sleep
from myfunctions import *
from datetime import datetime
#import time
import csv

from threading import Timer
from datetime import datetime

import threading


#Utility function
def killThreads(n=None, t=None):
    if n is None:
        n = ['Repeated Timer', 'Data logger']
    for t in threading.enumerate():
        if t.getName() in n:
            t.cancel()


# We can then kill any threads we know we've created if we have to...
killThreads()


#I think this is probably too complicated to teach
#There is a possibility instead of building in logic, eg to detect sensor type and then log it appropriately
#So eg beacon detector requires angle and distance?
#Detect using sensor .driver_name
class SensorDataLogger(object):
    def __init__(self, sensors=[], interval=0.1, maxSamples=20000, name='Data logger'):
        self.sensors = sensors
        self.interval = interval  # period between samples in seconds
        self.name = name
        self.results = []
        self.maxSamples=maxSamples
        # self.basetime =time.time()
        self.is_running = False
    def getsample(self):
        # now = time.time()
        # Maybe have a FIFO queue to drop early samples and retain more recent ones?
        # Or something more intelligent? eg drop every othersample? (so resample, essentially?)
        if len(self.results) <= self.maxSamples:
            result=[datetime.now()]
            for s in self.sensors:
                result.append(s.value())
            self.results.append(result)
    def _run(self):
        self.is_running = False
        self.start()
        self.getsample()
    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.setName(self.name)
            self._timer.start()
            self.is_running = True
    def stop(self):
        self._timer.cancel()
        self.is_running = False
        #killThreads(self.name)
        # return self.results
    def log(self):
        return self.results


cs=ColorSensor()
gs=GyroSensor()

dd=SensorDataLogger([cs,gs])
dd.start()
motors_on(FORWARDS,50)
sleep(10)
dd.stop()
motors_off()

#Could maybe get students to integrate this into the datalogger class, passing in filenmae etc?
with open("datalog.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(dd.log())