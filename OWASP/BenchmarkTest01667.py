
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-03/BenchmarkTest01667", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01667="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01667' in query string."

    param = query_string[param_loc + len(paramval):]  # 1st assume "BenchmarkTest01667" param is last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    return bar


class Test:

    def do_something(self, param):
        bar = "safe!"
        map96771 = {}
        map96771["keyA-96771"] = "a-Value"  # put some stuff in the collection
        map96771["keyB-96771"] = param  # put it in a collection
        map96771["keyC"] = "another-Value"  # put some stuff in the collection
        bar = map96771["keyB-96771"]  # get it back out

        return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
