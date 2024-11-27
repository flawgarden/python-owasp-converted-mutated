
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name)

@app.route("/sqli-01/BenchmarkTest00929", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00929")

    bar = None
    guess = "ABC"
    switchTarget = guess[2]

    # Simple case statement
    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bobs_your_uncle"
    elif switchTarget in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql.replace('?', 'foo'))
        results = statement.fetchall()
        # Assuming printResults is a defined function
        print_results(statement, sql, response)
    except sqlite3.DatabaseError as e:
        response.data = "Error processing request."
        return response
    return response

def print_results(statement, sql, response):
    # Implement result printing logic as per your requirements
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
