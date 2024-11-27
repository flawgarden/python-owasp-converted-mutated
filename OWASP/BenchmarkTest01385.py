
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01385", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest01385', '')

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

class Test:

    def do_something(self, param):
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

def get_sql_connection():
    # Replace with your actual database connection code
    return sqlite3.connect('yourdatabase.db')

def print_results(statement, sql, response):
    # Replace with your actual result printing code
    response.data = "Query executed successfully."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
