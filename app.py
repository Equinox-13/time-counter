from flask import Flask, render_template
from datetime import datetime


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/',)
def calculate_duration():
    while True:
        day = str((datetime.now() - datetime(2020,3,19)).days)
        sec = str((datetime.now() - datetime(2020,3,19)).seconds)
        micro = str((datetime.now() - datetime(2020,3,19)).microseconds)
        ans = {
            "days":day,
            "seconds":sec,
            "microseconds":micro,
        }
        return render_template('home.html', data=ans)


if __name__ == '__main__':
    app.run(debug = True)
