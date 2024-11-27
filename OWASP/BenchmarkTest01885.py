
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01885", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01885.html"))
        user_cookie = make_response("bar")
        user_cookie.set_cookie("BenchmarkTest01885", "bar", max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.set_cookie(user_cookie)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest01885" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest01885"])

        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            # Substitute the method for printing results
            print_results(cursor, sql)
            connection.close()
        except sqlite3.Error as e:
            return "Error processing request."
    return ""

def do_something(param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the first safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def print_results(cursor, sql):
    for row in cursor.fetchall():
        print(row)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
