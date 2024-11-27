
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02355", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02355":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        # Function to print results would be defined here
        return render_template("results.html", results=results)

    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
