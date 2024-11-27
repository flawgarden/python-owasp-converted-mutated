
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02089", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest02089")

    if headers:
        param = headers

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('your_database.db')
        cursor = connection.cursor()
        cursor.execute("PRAGMA read_uncommitted = 1")
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."
    
def do_something(param):
    bar = ""

    # Simple if statement that assigns constant to bar on true condition
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
