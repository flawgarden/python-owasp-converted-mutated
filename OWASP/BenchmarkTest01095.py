
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01095", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01095", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(cursor, sql)
        conn.close()
    except sqlite3.Error as e:
        return "Error processing request."

    return render_template("results.html", results=results)

class Test:
    def do_something(self, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

def print_results(cursor, sql):
    results = cursor.fetchall()
    # Logic to display results accordingly
    for row in results:
        print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
