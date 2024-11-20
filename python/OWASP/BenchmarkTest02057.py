
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02057", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    headers = request.headers.get('Referer')

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    if bar is not None:
        response.set_data(bar)
    
    return response

def do_something(param):
    bar = None
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
