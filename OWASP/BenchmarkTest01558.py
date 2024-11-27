
from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, param_name):
        return self.request.args.get(param_name)

class DatabaseHelper:
    @staticmethod
    def getSqlStatement():
        conn = sqlite3.connect('example.db')
        return conn.cursor()

    @staticmethod
    def printResults(cursor, sql, response):
        cursor.execute(sql)
        rows = cursor.fetchall()
        response_html = "<br>".join([str(row) for row in rows])
        response.get_writer().write(response_html)

@app.route("/sqli-03/BenchmarkTest01558", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = jsonify()
    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest01558")
    if param is None:
        param = ""

    bar = Test().doSomething(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement = DatabaseHelper.getSqlStatement()
        statement.execute(sql)
        DatabaseHelper.printResults(statement, sql, response)
    except sqlite3.Error as e:
        response.get_json()["error"] = "Error processing request."
        return response

    return response

class Test:
    def doSomething(self, param):
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
