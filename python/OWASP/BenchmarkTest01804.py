
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-03/BenchmarkTest01804", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01804")
    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        print_results(cursor, sql)
        connection.close()
    except sqlite3.Error as e:
        print("Error processing request.")
        return

class Test:

    def do_something(self, param):
        bar = "safe!"
        map31481 = {}
        map31481["keyA-31481"] = "a_Value"
        map31481["keyB-31481"] = param
        map31481["keyC"] = "another_Value"
        bar = map31481["keyB-31481"]
        bar = map31481["keyA-31481"]
        return bar

def print_results(cursor, sql):
    print("SQL Query: ", sql)
    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
