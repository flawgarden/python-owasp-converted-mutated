
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-02/BenchmarkTest01218", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()

    param = ""
    if 'BenchmarkTest01218' in request.headers:
        param = request.headers['BenchmarkTest01218']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        response_data = statement.fetchall()
        response.write(str(response_data))
    except sqlite3.Error as e:
        response.write("Error processing request.")
        return response

    return response

class Test:
    def do_something(self, param):
        bar = ""
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
