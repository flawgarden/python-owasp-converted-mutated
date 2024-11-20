
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00287", methods=['GET', 'POST'])
def benchmark_test_00287():
    if request.method == 'GET':
        return benchmark_test_00287_post()
    return benchmark_test_00287_post()

def benchmark_test_00287_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = param

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar is not None:
        length = len(bar)
        response.response = [bar[:length]]
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
