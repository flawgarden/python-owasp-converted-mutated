
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00146", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get('Referer', '')
    param = urllib.parse.unquote(param)

    bar = param
    if param and len(param) > 1:
        sbxyz67327 = list(param)
        bar = ''.join(sbxyz67327[:-1] + ['Z'])

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(bar % tuple(obj))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
