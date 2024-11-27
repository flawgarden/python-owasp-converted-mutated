
import urllib.parse
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01178", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(req):
    param = ""
    referer = req.headers.get('Referer')

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = Test().do_something(req, param)

    response = app.response_class(
        response=bar,
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:
    def do_something(self, req, param):
        sbxyz69428 = str(param)
        bar = sbxyz69428 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
