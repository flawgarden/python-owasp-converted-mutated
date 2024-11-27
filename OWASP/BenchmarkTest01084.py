
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01084", methods=['GET', 'POST'])
def benchmark_test_01084():
    if request.method == 'GET':
        return benchmark_test_01084_post()

    return benchmark_test_01084_post()

def benchmark_test_01084_post():
    response = "text/html;charset=UTF-8"
    
    param = request.headers.get("BenchmarkTest01084", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        
        return print_results(cursor, sql)
    except sqlite3.Error as e:
        return "Error processing request."

def print_results(cursor, sql):
    # Mock-up function to simulate the result handling
    return f"Executed SQL: {sql}, Results: {cursor.fetchall()}"

class Test:
    def do_something(self, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        return "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
