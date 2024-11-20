
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Replace with your database
    return conn.cursor()

@app.route("/sqli-04/BenchmarkTest01889", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01889.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01889", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return user_cookie

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if "BenchmarkTest01889" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest01889"])

        bar = do_something(request, param)

        sql = "INSERT INTO users (username, password) VALUES ('foo', '" + bar + "')"

        try:
            statement = get_sql_statement()
            count = statement.execute(sql)
            statement.connection.commit()
            return "Update complete"
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
