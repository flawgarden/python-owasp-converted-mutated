
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-01/BenchmarkTest00841", methods=['GET', 'POST'])
def benchmark_test_00841():
    if request.method == 'GET':
        return benchmark_test_00841_post()

    return benchmark_test_00841_post()


def benchmark_test_00841_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00841="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00841' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target == 'C' or switch_target == 'D':
        bar = param
    else:
        bar = "bobs_your_uncle"

    try:
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        # Placeholder for the actual database call
        # DatabaseHelper.JDBCtemplate.batchUpdate(sql)

        return f"No results can be displayed for query: {sql}<br> because the Spring batchUpdate method doesn't return results."
    except Exception as e:
        return "Error processing request."


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
