
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-04/BenchmarkTest01884", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01884.html"))
        user_cookie = 'BenchmarkTest01884=bar; Max-Age=180; Secure; Path=/sqli-04/BenchmarkTest01884; Domain=' + request.host
        response.set_cookie("BenchmarkTest01884", "bar", max_age=180, secure=True, path=request.path, domain=request.host)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01884' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01884'])

        bar = do_something(request, param)

        try:
            sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
            # Assuming a mock version of the JDBC template batch update
            # DatabaseHelper.JDBCtemplate.batchUpdate(sql)
            return f"No results can be displayed for query: {sql}<br>because the Spring batchUpdate method doesn't return results."
        except Exception as e:
            return "Error processing request."

def do_something(request, param):
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
