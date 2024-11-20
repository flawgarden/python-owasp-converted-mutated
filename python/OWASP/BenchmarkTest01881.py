
import os
from flask import Flask, request, render_template, make_response, url_for
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01881", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("sqli-04/BenchmarkTest01881.html"))
        user_cookie = 'BenchmarkTest01881=bar; Max-Age=180; Secure; Path={}; Domain={}'.format(
            request.path,
            request.host
        )
        resp.set_cookie('BenchmarkTest01881', 'bar', max_age=180, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest01881' in the_cookies:
            param = unquote(the_cookies['BenchmarkTest01881'])

        bar = do_something(request, param)

        try:
            sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
            # Assuming DatabaseHelper.JDBCtemplate.batchUpdate is defined elsewhere
            # DatabaseHelper.JDBCtemplate.batchUpdate(sql)
            return "No results can be displayed for query: " + sql + "<br> because the Spring batchUpdate method doesn't return results."
        except Exception as e:
            return "Error processing request."

def do_something(request, param):
    bar = "safe!"
    map_ = {}
    map_["keyA-20027"] = "a-Value"
    map_["keyB-20027"] = param
    map_["keyC"] = "another-Value"
    bar = map_["keyB-20027"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
