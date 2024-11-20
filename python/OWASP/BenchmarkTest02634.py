
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    # Replace with your database connection details
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-05/BenchmarkTest02634", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02634="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02634' in query string."

    param = query_string[param_loc + len(paramval):] 
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME=? and PASSWORD='{bar}'"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql, ('foo',))
        results = cursor.fetchall()
        connection.close()
        return str(results)  # Replace with your desired format to render results
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
