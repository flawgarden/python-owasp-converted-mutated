
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00049", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request()

    return handle_request()

def handle_request():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00049" + "="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.set_data("getQueryString() couldn't find expected parameter 'BenchmarkTest00049' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data("Parameter value: " + param)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
