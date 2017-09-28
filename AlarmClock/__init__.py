from AlarmClock import AlarmThread
from datetime import datetime, timedelta, time, date

def printTrigger():
    print("Alarm!")

class AlarmClock:
    def __init__(self, trigger=printTrigger):
        self.alarm_thread = AlarmThread.AlarmThread(trigger)

    def set_alarm(self, hour, minute):
        today = date.today()
        alarm_time = time(hour=hour, minute=minute)

        alarm = datetime.combine(today, alarm_time)

        if alarm < datetime.now():
            alarm = alarm + timedelta(days=1)

        self.alarm_thread.set_alarm(alarm)

    def get_alarm(self):
        return self.alarm_thread.alarm
