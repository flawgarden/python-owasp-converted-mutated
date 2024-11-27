
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn.cursor(), conn

@app.route("/sqli-02/BenchmarkTest01091", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    if 'BenchmarkTest01091' in request.headers:
        param = request.headers['BenchmarkTest01091']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement, conn = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        response.set_data("Error processing request.")
        return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = []
            values_list.append("safe")
            values_list.append(param)
            values_list.append("moresafe")

            values_list.pop(0)

            bar = values_list[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
