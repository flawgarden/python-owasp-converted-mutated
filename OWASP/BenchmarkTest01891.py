
import os
from flask import Flask, request, render_template, make_response, redirect, url_for
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-04/BenchmarkTest01891", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01891.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest01891=bar; Max-Age=180; Secure; Path=" + request.path)
        response.headers.add("Set-Cookie", "BenchmarkTest01891=bar; Max-Age=180; Secure; Path=" + request.path)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01891' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01891'])

        bar = do_something(request, param)
        sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

        try:
            statement = get_sql_statement()
            statement.execute(sql)
            get_sql_statement().connection.commit()
            output_update_complete(sql)
        except sqlite3.Error as e:
            return "Error processing request."

def do_something(request, param):
    bar = param
    num = 106
    return bar if (7 * 42) - num <= 200 else "This should never happen"

def output_update_complete(sql):
    return f"SQL update complete: {sql}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
