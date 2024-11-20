
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-01/BenchmarkTest00799", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00799="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.set_data("getQueryString() couldn't find expected parameter 'BenchmarkTest00799' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[1]

    response.headers['X-XSS-Protection'] = '0'
    obj = ("a", bar)
    response.set_data("<!DOCTYPE html>\n<html>\n<body>\n<p>")
    response.set_data(response.get_data(as_text=True) + "Formatted like: %s and %s." % obj)
    response.set_data(response.get_data(as_text=True) + "\n</p>\n</body>\n</html>")

    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
