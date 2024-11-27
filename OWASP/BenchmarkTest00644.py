
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00644", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return process_request(request)
    return process_request(request)

def process_request(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest00644", "")
    if not param:
        param = ""

    bar = ""
    if param:
        bar = param.split(" ")[0]

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar.encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
