
from flask import Flask, request, render_template
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-03/BenchmarkTest01725", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01725="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01725' in query string."

    param = query_string[param_loc + len(paramval):]  # 1st assume "BenchmarkTest01725" param is last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = unquote(param)
    bar = Test().do_something(param)

    sql = "SELECT USERNAME FROM USERS WHERE USERNAME='foo' AND PASSWORD='{}' LIMIT 1".format(bar)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()

        if result:
            return "Your results are: " + result[0]
        return "No results returned for query: " + sql

    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        # Simulate the interaction with the Thing interface
        bar = self.some_processing(param)
        return bar

    def some_processing(self, param):
        # Add actual processing logic here if necessary
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
