
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-04/BenchmarkTest01887", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01887.html"))
        user_cookie = make_response("bar")
        user_cookie.set_cookie("BenchmarkTest01887", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie(user_cookie)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if the_cookies:
            param = the_cookies.get("BenchmarkTest01887", param)
            param = unquote(param)

        bar = do_something(param)
        sql = f"INSERT INTO users (username, password) VALUES ('foo', '{bar}')"

        try:
            conn, cursor = get_sql_statement()
            cursor.execute(sql)
            conn.commit()
            return "Update complete", 200
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
