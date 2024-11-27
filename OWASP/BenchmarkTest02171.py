
import os
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02171", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02171', default='', type=str)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('your_database.db')  # replace with your database
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(results, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(param):
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    else:
        bar = ""
    return bar

def print_results(results, sql, response):
    # Implement your result printing logic here
    for row in results:
        response.data += str(row) + "<br />"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
