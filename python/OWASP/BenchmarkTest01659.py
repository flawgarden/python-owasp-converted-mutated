
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01659", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)

def do_get(request):
    return do_post(request)

def do_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01659="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01659' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    
    bar = Test().do_something(request, param)

    return bar

class Test:
    @staticmethod
    def do_something(request, param):
        bar = escape(param)
        return bar

def escape(param):
    return urllib.parse.quote(param)  # Simple HTML escaping

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
