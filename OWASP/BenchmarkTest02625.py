
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02625", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02625="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02625' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('database.db')  # Adjust based on your database configuration
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return str(results)  # or format results as needed
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = "safe!"
    map_82391 = {
        "keyA-82391": "a-Value",
        "keyB-82391": param,
        "keyC": "another-Value"
    }
    bar = map_82391.get("keyB-82391")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')