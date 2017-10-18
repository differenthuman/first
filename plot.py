import plotly
plotly.tools.set_credentials_file(username="differenthuman", api_key="I3gkp3DL4OImAzyZMYAU")

import plotly.plotly as py
import plotly.graph_objs as go

stream_id = "5tj8lxf9qd"
stream_1 = dict(token=stream_id, maxpoints=60)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1
    )

data = go.Data([trace1])

layout = go.Layout(title='Time Series')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename = "python-streaming")

s = py.Stream(stream_id)
s.open()

import datetime
import time
import random

time.sleep(5)
n = 0
k = 0
while True:
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    y = random.random()
    n = k*n+y
    k = k+1
    n = n/k

    s.write(dict(x = x, y = n))

    time.sleep(1)
s.close
