
from flask import Flask, request, render_template, make_response
import sqlite3
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-04/BenchmarkTest01879", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("sqli-04/BenchmarkTest01879.html"))
        resp.set_cookie("BenchmarkTest01879", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if "BenchmarkTest01879" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest01879"])

        bar = do_something(param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_db_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            print_results(results, sql)
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[1]
    return bar

def print_results(results, sql):
    # Logic to print or render results
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
