
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00148", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    if request.headers.get("Referer"):
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    response.headers['X-XSS-Protection'] = "0"
    response.data = f"Formatted like: {'a'} and {bar}."
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
