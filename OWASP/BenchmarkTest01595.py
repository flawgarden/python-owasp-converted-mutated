
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01595", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class(content_type="text/html;charset=UTF-8")

        values = request.form.getlist("BenchmarkTest01595")
        param = values[0] if values else ""

        bar = Test().do_something(param)

        response.headers["X-XSS-Protection"] = "0"
        response.set_data(bar)

        return response

class Test:

    @staticmethod
    def do_something(param):
        from html import escape
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
