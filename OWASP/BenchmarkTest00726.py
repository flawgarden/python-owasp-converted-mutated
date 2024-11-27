
from flask import Flask, request, Response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00726", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00726")
    param = values[0] if values else ""

    bar = html.escape(param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
