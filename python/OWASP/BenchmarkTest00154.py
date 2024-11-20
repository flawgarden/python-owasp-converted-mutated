
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00154", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    if 'Referer' in request.headers:
        param = request.headers['Referer']

    param = urllib.parse.unquote(param)

    bar = ''
    guess = "ABC"
    switchTarget = guess[2]

    if switchTarget == 'A':
        bar = param
    elif switchTarget == 'B':
        bar = "bobs_your_uncle"
    elif switchTarget in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
