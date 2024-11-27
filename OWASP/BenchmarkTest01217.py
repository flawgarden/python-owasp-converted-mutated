
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01217", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = "text/html;charset=UTF-8"
    param = ""
    headers = request.headers.get("BenchmarkTest01217")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('your_database.db')  # Adjust to your database
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(sql, results)
    except sqlite3.Error as e:
        return f"Error processing request: {str(e)}"

class Test:

    def do_something(self, request, param):
        a89502 = param
        b89502 = str(a89502) + " SafeStuff"
        b89502 = b89502[:-len("Chars")] + "Chars"
        map89502 = {}
        map89502["key89502"] = b89502
        c89502 = map89502["key89502"]
        d89502 = c89502[:-1]
        e89502 = d89502.encode('utf-8').decode('unicode_escape')

        f89502 = e89502.split(" ")[0]
        g89502 = "barbarians_at_the_gate"
        bar = g89502  # static so this whole flow is 'safe'

        return bar

def print_results(sql, results):
    print(f"SQL: {sql}")
    print("Results:", results)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
