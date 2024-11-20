
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_for_list(sql):
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results
    except Exception as e:
        raise e

@app.route("/sqli-04/BenchmarkTest02178", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02178", "")
    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        list_results = query_for_list(sql)
        response += "Your results are: <br>"
        for o in list_results:
            response += str(o) + "<br>"
    except Exception as e:
        response += "Error processing request."
    return response

def do_something(param):
    bar = "safe!"
    map38026 = {}
    map38026["keyA-38026"] = "a-Value"
    map38026["keyB-38026"] = param
    map38026["keyC"] = "another-Value"
    bar = map38026["keyB-38026"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
