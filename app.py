from flask import Flask, render_template
from dateutil.relativedelta import relativedelta
from datetime import datetime


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/',)
def calculate_duration():
    year = str(relativedelta(datetime.now(),datetime(2020,3,19)).years)
    mon = str(relativedelta(datetime.now(),datetime(2020,3,19)).months)
    day = str(relativedelta(datetime.now(),datetime(2020,3,19)).days)
    hour = str(relativedelta(datetime.now(),datetime(2020,3,19)).hours)
    minute = str(relativedelta(datetime.now(),datetime(2020,3,19)).minutes)
    sec = str(relativedelta(datetime.now(),datetime(2020,3,19)).seconds)
    micro = str(relativedelta(datetime.now(),datetime(2020,3,19)).microseconds)
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
