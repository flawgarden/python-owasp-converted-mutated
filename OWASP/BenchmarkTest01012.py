
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    # Replace with your database connection logic
    conn = sqlite3.connect('your_database.db')  # Example connection
    return conn.cursor()

@app.route("/sqli-02/BenchmarkTest01012", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest01012.html"))
        user_cookie = make_response("cookie set")
        user_cookie.set_cookie("BenchmarkTest01012", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest01012' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01012'])

        bar = Test().do_something(request, param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            statement = get_sql_statement()
            statement.execute(sql)
            # Assuming you have a function to print results:
            print_results(statement, sql)
        except sqlite3.Error as e:
            return "Error processing request."

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def print_results(statement, sql):
    # Implement your result printing logic here
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
