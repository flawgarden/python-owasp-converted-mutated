
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02053", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer  # just grab the first element

    param = urllib.parse.unquote(param)  # URL decode the header value

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data('Formatted like: %s and %s.' % (bar, 'b'))
    return response

def do_something(param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
