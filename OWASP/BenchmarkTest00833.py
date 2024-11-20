
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00833", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest00833="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00833' in query string."

    param = query_string[param_loc + len(paramval):]  # assume param is last in query string
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    request.environ['wsgi.session']['userid'] = bar

    return "Item: 'userid' with value: '{}' saved in session.".format(bar)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
