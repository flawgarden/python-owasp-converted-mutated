
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00150", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('Referer', '')
    param = urllib.parse.unquote(param)

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    response = make_response()
    response.headers['X-XSS-Protection'] = '0'
    response.set_data(f"Formatted like: a and {bar}.")
    response.mimetype = "text/html;charset=UTF-8"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
