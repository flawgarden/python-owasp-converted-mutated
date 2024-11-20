
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01628", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ''
    values = request.args.getlist("BenchmarkTest01628")
    param = values[0] if values else ''

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        response = print_results(statement, sql)
    except sqlite3.Error as e:
        response = "Error processing request."

    return response

class Test:

    def do_something(self, param):
        bar = ''
        guess = "ABC"
        switch_target = guess[1] 

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

def print_results(statement, sql):
    statement.execute(sql)
    results = statement.fetchall()
    return str(results)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
