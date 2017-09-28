from flask import Flask, render_template, request, redirect
import AlarmClock

app = Flask(__name__)

alarmclock = AlarmClock.AlarmClock()

@app.route('/')
def index():
    alarm = alarmclock.get_alarm()
    if alarm is None:
        time = "No Alarm!"
    else:
        minute = alarm.minute
        if minute == 0:
            minute = '00'
        time = "{}:{}".format(alarm.hour, minute)
    return render_template('index.html', title='Wecker', next_alarm=time)


@app.route('/set-alarm', methods=['post'])
def new_alarm():
    str_time = request.form['time']
    print(str_time)
    time = str_time.split(':')
    alarmclock.set_alarm(int(time[0]), int(time[1]))
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
