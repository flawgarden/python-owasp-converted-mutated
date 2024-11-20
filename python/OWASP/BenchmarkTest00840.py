
import os
from flask import Flask, request, render_template
import urllib.parse
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00840", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00840="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00840' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
        
    param = urllib.parse.unquote(param)

    bar = None

    # Simple ? condition that assigns param to bar on false condition
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Simulating database update
        # org.owasp.benchmark.helpers.DatabaseHelper.JDBCtemplate.batchUpdate(sql) would be implemented here

        return "No results can be displayed for query: " + sql + "<br>because the Spring batchUpdate method doesn't return results."
    except Exception as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
