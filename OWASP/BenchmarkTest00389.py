
from flask import Flask, request, Response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00389", methods=['GET', 'POST'])
def benchmark_test_00389():
    if request.method == 'GET':
        return benchmark_test_00389_post()
    return benchmark_test_00389_post()

def benchmark_test_00389_post():
    param = request.args.get('BenchmarkTest00389', '')
    bar = html.escape(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

@app.errorhandler(404)
def page_not_found(e):
    return Response("404 Not Found", status=404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
