
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00375", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get('BenchmarkTest00375', '')
    bar = param.split(" ")[0] if param else ""

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(response.response_formatter(bar, obj))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
