
from flask import Flask, request, Response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-06/BenchmarkTest02648", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02648="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02648' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        return str(results)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = "safe!"
    map91488 = {}
    map91488["keyA-91488"] = "a_Value"
    map91488["keyB-91488"] = param
    map91488["keyC"] = "another_Value"
    bar = map91488["keyB-91488"]
    bar = map91488["keyA-91488"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
