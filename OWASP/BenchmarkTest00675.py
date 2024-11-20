
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, name):
        return self.request.args.get(name)

def get_sql_connection():
    return sqlite3.connect('your_database.db')

@app.route("/sqli-01/BenchmarkTest00675", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00675")
    if param is None:
        param = ""

    bar = param if (7 * 42) - 86 <= 200 else "This_should_always_happen"

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        # assuming a helper function to print results
        print_results(statement, sql, response)
        connection.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def print_results(statement, sql, response):
    # Dummy implementation for results printing
    response.data += f"<br>Executed SQL: {sql}<br>Results: {statement.fetchall()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
