
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01083", methods=['GET', 'POST'])
def benchmark_test_01083():
    if request.method == 'GET':
        return benchmark_test_01083_post()
    return benchmark_test_01083_post()

def benchmark_test_01083_post():
    param = request.headers.get("BenchmarkTest01083", "")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql, ("foo",))
        rows = statement.fetchall()
        return render_template("results.html", results=rows)
    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, param):
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
