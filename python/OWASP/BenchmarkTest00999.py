
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest00999", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest00999.html"))
        user_cookie = ('BenchmarkTest00999', 'verifyUserPassword%28%27foo%27%2C%27bar%27%29', 60 * 3, True)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3], path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest00999' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00999'])

        bar = Test().do_something(param)

        sql = "{call " + bar + "}"

        try:
            connection = get_sql_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print_results(results, sql)
        except sqlite3.Error as e:
            return "Error processing request."

class Test:

    def do_something(self, param):
        bar = param
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        return bar

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')
    return conn

def print_results(results, sql):
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
