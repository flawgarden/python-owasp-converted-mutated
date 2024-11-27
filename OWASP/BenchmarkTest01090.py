
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-02/BenchmarkTest01090", methods=['POST', 'GET'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = request.headers.get("BenchmarkTest01090", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        print_results(sql, results)
    except sqlite3.Error:
        return "Error processing request.", 500

def print_results(sql, results):
    print("SQL: ", sql)
    print("Results: ", results)

class Test:
    
    def do_something(self, request, param):
        bar = "safe!"
        map_holder = {}
        map_holder["keyA-12212"] = "a-Value"
        map_holder["keyB-12212"] = param
        map_holder["keyC"] = "another-Value"
        bar = map_holder.get("keyB-12212")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
