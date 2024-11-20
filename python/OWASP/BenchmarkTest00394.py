
import os
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00394", methods=['GET', 'POST'])
def benchmark_test00394():
    if request.method == 'POST':
        return benchmark_test00394_post(request)
    return benchmark_test00394_get(request)

def benchmark_test00394_get(request):
    return benchmark_test00394_post(request)

def benchmark_test00394_post(request):
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00394', default='', type=str)

    bar = "alsosafe"
    if param:
        valuesList = []
        valuesList.append("safe")
        valuesList.append(param)
        valuesList.append("moresafe")

        valuesList.pop(0)

        bar = valuesList[1]

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar:
        length = len(bar)
        response.response = bar[:length]
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
