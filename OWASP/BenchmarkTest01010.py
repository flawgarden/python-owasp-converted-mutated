
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-02/BenchmarkTest01010", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest01010.html"))
        user_cookie = ('BenchmarkTest01010', 'bar', 60 * 3, request.path, request.host_url)
        response.set_cookie(*user_cookie)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01010' in the_cookies:
            param = unquote(the_cookies['BenchmarkTest01010'])

        bar = Test().do_something(request, param)

        try:
            sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
            # Simulating a database operation
            # DatabaseHelper.JDBCtemplate.batchUpdate(sql)
            return "No results can be displayed for query: " + sql + "<br> because the Spring batchUpdate method doesn't return results."
        except Exception as e:
            return "Error processing request."

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
