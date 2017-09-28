from threading import Thread, Event
from time import sleep
from datetime import datetime, timedelta


class AlarmThread(Thread):
    def __init__(self, trigger):
        Thread.__init__(self,)
        self.alarm = None
        self.trigger = trigger

    def run(self):
        while True:
            if self.alarm is None:
                return

            if self.alarm < datetime.now():
                self.trigger()
                return

            sleep(1)

    def set_alarm(self, alarm):
        self.alarm = alarm
        if not self.is_alive():
            self.start()
