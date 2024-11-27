
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02265", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = ""

    map = request.args.to_dict()
    if map:
        values = map.get("BenchmarkTest02265")
        if values is not None:
            param = values

    bar = do_something(param)

    sql = "{call " + bar + "}"

    try:
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql, response)
    except sqlite3.Error as e:
        response = "Error processing request."
        return response

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def print_results(results, sql, response):
    for row in results:
        print(row)  # Replace with your actual result printing logic
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
