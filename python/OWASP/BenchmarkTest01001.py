
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01001", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest01001.html"))
        user_cookie = make_response("BenchmarkTest01001=bar")
        user_cookie.set_cookie("BenchmarkTest01001", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.headers.add('Set-Cookie', user_cookie)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if "BenchmarkTest01001" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest01001"])

        bar = Test().do_something(request, param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            statement = connection.execute(sql, ("foo",))
            results = statement.fetchall()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
