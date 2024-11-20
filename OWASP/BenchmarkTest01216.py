
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01216", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    headers = request.headers.get("BenchmarkTest01216")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('database.db')  # Replace with your database connection details
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(sql, results, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."

    return response

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)

            bar = values_list[1]

        return bar

def print_results(sql, results, response):
    response.data = f"Executed SQL: {sql} <br> Results: {results}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
