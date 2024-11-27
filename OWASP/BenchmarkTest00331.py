
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00331", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest00331")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map59781 = {
        "keyA-59781": "a_Value",
        "keyB-59781": param,
        "keyC": "another_Value"
    }
    bar = map59781["keyB-59781"]
    bar = map59781["keyA-59781"]

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')  # Adjust your database path as needed
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        connection.close()
        return render_template("results.html", results=results)

    except sqlite3.Error as e:
        response = "Error processing request."
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
