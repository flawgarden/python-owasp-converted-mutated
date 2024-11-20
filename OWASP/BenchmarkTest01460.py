
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01460", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01460":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    sql = "{call " + bar + "}"

    try:
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        # Implement printResults equivalent here
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request.", 500

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-72098": "a-Value",
            "keyB-72098": param,
            "keyC": "another-Value"
        }
        bar = map_.get("keyB-72098")

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
