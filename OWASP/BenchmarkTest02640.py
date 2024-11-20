
import os
from flask import Flask, request, render_template
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-05/BenchmarkTest02640", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02640="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02640' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = unquote(param)

    bar = do_something(param)

    try:
        sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='" + bar + "'"
        # Replace with your database execution logic
        # Example: DatabaseHelper.JDBCtemplate.execute(sql)

        return "No results can be displayed for query: " + sql + "<br> because the execute method doesn't return results."
    except Exception as e:
        return "Error processing request."


def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bob's your uncle"

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
