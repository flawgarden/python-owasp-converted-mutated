
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-04/BenchmarkTest01880", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01880.html"))
        user_cookie = 'BenchmarkTest01880=bar; Max-Age=180; Secure; Path=' + request.path + '; Domain=' + request.host
        response.set_cookie("BenchmarkTest01880", "bar", max_age=180, secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest01880" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest01880"])

        bar = do_something(param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')  # Change to your DB connection method
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            print_results(results, sql)
            connection.close()
        except sqlite3.Error as e:
            print("Error processing request.")

    return render_template("sqli-04/BenchmarkTest01880.html")


def do_something(param):
    bar = "safe!"
    map99153 = {}
    map99153["keyA-99153"] = "a_Value"
    map99153["keyB-99153"] = param
    map99153["keyC"] = "another_Value"
    bar = map99153["keyB-99153"]
    bar = map99153["keyA-99153"]

    return bar


def print_results(results, sql):
    for row in results:
        print(row)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
