
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00301", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'Referer' in request.headers:
        param = request.headers['Referer']

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map16074 = {}
    map16074["keyA-16074"] = "a-Value"
    map16074["keyB-16074"] = param
    map16074["keyC"] = "another-Value"
    bar = map16074["keyB-16074"]

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(f"Parameter value: {bar}")
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
