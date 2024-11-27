
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-00/BenchmarkTest00283", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()


def benchmark_test_post():
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = escape(param)  # Replace ESAPI.encoder().encodeForHTML with a similar Flask escape function
    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response


def escape(text):
    from markupsafe import escape
    return escape(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
