## Plotly Dash

Dash is a productive Python framework for building web analytic applications.

Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. [1]

#### Why use Dash?

The Good Reasons to Build a Dashboard with Dash
1. Open Source Tool: Dash is a great alternative BI tools to Tableau or Microsoft Power BI because it is costly to operate dashboards built by Tableau or Power BI. Dash provides similar quality and experience at no cost.
2. Run in Python: Dash runs in Python. You may use Pandas and any Python library for the pipeline and render the visualization with Dash.
3. Great Appearance: Dash and pure Plotlyare built on top of d3, it means Dash and pure Plotly make high quality visualizations which is comparable with Tableau charts.
4. Integrated with Pure Plotly: Plotly is one of the great open source visualization package in Python. If you know how to use Plotly, it does not take a long time to understand Dash. At the same time, you may also visualize your existing Plotly graphs on Dash with a little code editing.
5. Integrated with Flask: Dash runs web server in Flask. One of the nice features about Dash is that you do not need to set up Flask and it is easy to host the webserver in AWS. You do not need to know too much about web development.
6. Easy-to-use: Dash is a high level tool that the developers are only required to write in Python and have some understanding of html. No Javascript or d3 is needed to produce the dashboard. You may also leverage the interactive elements available in d3 with Python code. Dash is very customizable that eliminates the constraint of pure Plotly. [2]


Further Reading: <br>
[[1] Plotly Dash Intro](https://dash.plotly.com/introduction) <br>
[[2] @jjsham's blog on Medium](https://medium.com/@jjsham/building-dashboard-using-plotly-dash-36bf94a1137)<br>
[[3] Dash Sample Applications](https://github.com/plotly/dash-sample-apps) <br>
[[4] Dash for Beginners](https://www.datacamp.com/community/tutorials/learn-build-dash-python)


### Requirements

```
pip install plotly
pip install dash
```

### Getting Started

Start the server my going into the directory of the dashboard and entering the below command on Command prompt/Terminal:
```
python your_app_name.py
```

This will start the server & you should be able to view the dashboard by visiting http://127.0.0.1:8050/



