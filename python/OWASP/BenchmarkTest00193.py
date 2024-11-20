
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00193", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00193", "")
    param = urllib.parse.unquote(param)

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')  # Replace with actual database connection
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
