from AlarmClock.AlarmThread import AlarmThread
from datetime import datetime, timedelta

def trigger():
    print("ALARM!!!!")


thread = AlarmThread(trigger)

alarm = datetime.now()+timedelta(seconds=5)

print("Set Alarm")

thread.set_alarm(alarm)