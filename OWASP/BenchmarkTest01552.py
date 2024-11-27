
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')  # replace with your database path
    return conn

@app.route("/sqli-03/BenchmarkTest01552", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(response='', content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest01552', '')
    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request." if True else str(e)

    return response

class Test:
    def do_something(self, param):
        bar = param
        return bar

def print_results(statement, sql, response):
    # Implement your result printing logic here
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
