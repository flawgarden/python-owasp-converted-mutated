
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01348", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest01348", "")

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = bar
    return response

class Test:

    def do_something(self, request, param):
        from html import escape
        bar = escape(param)
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
