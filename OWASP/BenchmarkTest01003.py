
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    # Simulating the connection to a database
    return sqlite3.connect('your_database.db')

@app.route("/sqli-02/BenchmarkTest01003", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest01003.html"))
        user_cookie = make_response("Cookie Set")
        user_cookie.set_cookie("BenchmarkTest01003", "bar", max_age=60 * 3, secure=True, path=request.path)
        response.set_cookie(**user_cookie.cookies)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if "BenchmarkTest01003" in cookies:
            param = unquote(cookies["BenchmarkTest01003"])

        bar = Test().do_something(param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            # Assuming print_results mimics org.owasp.benchmark.helpers.DatabaseHelper.printResults
            return str(results)  # or render with a template
        except sqlite3.Error as e:
            return "Error processing request."

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
