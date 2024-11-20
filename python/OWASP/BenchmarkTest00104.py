
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-00/BenchmarkTest00104", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-00/BenchmarkTest00104.html"))
        user_cookie = 'BenchmarkTest00104=bar'
        response.set_cookie("BenchmarkTest00104", "bar", max_age=60*3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        
        if 'BenchmarkTest00104' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00104'])

        bar = param if (7 * 42) - 86 <= 200 else "This_should_always_happen"

        try:
            sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
            # Assuming DatabaseHelper is defined somewhere in your app for executing SQL
            # DatabaseHelper.JDBCtemplate.batchUpdate(sql)
            return "No results can be displayed for query: " + sql + "<br>" + " because the Spring batchUpdate method doesn't return results."
        except Exception as e:
            return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
