from flask import Flask, render_template
from dateutil.relativedelta import relativedelta
from datetime import datetime


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/',)
def calculate_duration():
    duration = relativedelta(datetime.now(),datetime(2020,3,19))
    year = str(duration.years)
    mon = str(duration.months)
    day = str(duration.days)
    hour = str(duration.hours)
    minute = str(duration.minutes)
    sec = str(duration.seconds)
    micro = str(duration.microseconds)
    res = {
        "years":year,
        "months":mon,
        "days":day,
        "hours":hour,
        "minutes":minute,
        "seconds":sec,
        "microseconds":micro,
    }
    return render_template('home.html', data=res)


if __name__ == '__main__':
    app.run(debug = True)
