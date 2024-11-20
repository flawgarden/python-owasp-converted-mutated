
from flask import Flask, request, render_template
import sqlite3
from contextlib import closing

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:

    @staticmethod
    def get_sql_connection():
        # Assuming SQLite for demonstration; Modify for actual use case
        return sqlite3.connect('database.db')

    @staticmethod
    def print_results(statement, sql, response):
        results = statement.fetchall()
        for row in results:
            response.write(str(row))

class SeparateClassRequest:

    def __init__(self, request):
        self.request = request

    def get_the_value(self, key):
        return self.request.args.get(key)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_10271 = {}
        map_10271["keyA-10271"] = "a_Value"
        map_10271["keyB-10271"] = param
        map_10271["keyC"] = "another_Value"
        bar = map_10271["keyB-10271"]
        bar = map_10271["keyA-10271"]
        return bar

@app.route("/sqli-03/BenchmarkTest01805", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = request.environ.get('wsgi.errors')
    param = SeparateClassRequest(request).get_the_value("BenchmarkTest01805")
    bar = Test().do_something(request, param)
    
    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        with closing(DatabaseHelper.get_sql_connection()) as connection:
            statement = connection.execute(sql, ("foo",))
            DatabaseHelper.print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.write("Error processing request.")
        return

if __name__ == "__main__":
    app.run(host='0.0.0.0')
