
import os
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

@app.route("/sqli-04/BenchmarkTest01890", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response(render_template("sqli-04/BenchmarkTest01890.html"))
    
    if request.method == 'GET':
        user_cookie = response.set_cookie("BenchmarkTest01890", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest01890' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest01890'])

        bar = do_something(param)
        sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

        try:
            statement = get_sql_statement()
            statement.execute(sql, (bar,))
            response_msg = "SQL update completed."
            response.get_data(as_text=True)
        except sqlite3.Error as e:
            response = make_response("Error processing request.")
            return response

    return response

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
