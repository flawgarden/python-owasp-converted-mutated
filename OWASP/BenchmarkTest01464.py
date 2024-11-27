
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-03/BenchmarkTest01464", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01464":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')  # Adjust the connection as necessary
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
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

def print_results(statement, sql, response):
    # Implement a function to format and display results appropriately
    response.data = str(statement.fetchall())
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
