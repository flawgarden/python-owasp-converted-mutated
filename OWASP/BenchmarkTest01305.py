
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01305", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest01305', '')

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql, ('foo',))
        results = cursor.fetchall()
        # Assuming you have a function to print results
        print_results(cursor, sql, response)
    except sqlite3.Error:
        response.data = "Error processing request."
        return response

    return response

class Test:

    def do_something(self, param):
        bar = ''

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

def print_results(cursor, sql, response):
    # Convert cursor results to string and assign to response data
    rows = cursor.fetchall()
    response.data = str(rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
