
import os
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-02/BenchmarkTest01302", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01302", "")
    
    bar = Test().do_something(param)
    
    sql = "{call " + bar + "}"
    
    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)
    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

def print_results(results, sql):
    # Implement printing results logic based on your needs
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
