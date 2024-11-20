
from flask import Flask, request

app = Flask(__name__)

@app.route("/xss-05/BenchmarkTest02493", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_post(request)

def do_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.values.getlist("BenchmarkTest02493")
    param = values[0] if values else ""

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    length = 1
    if bar:
        length = len(bar)
        response.data = bar.encode('utf-8')[:length]

    return response

def do_something(request, param):
    bar = "safe!"
    map4720 = {}
    map4720["keyA-4720"] = "a-Value"
    map4720["keyB-4720"] = param
    map4720["keyC"] = "another-Value"
    bar = map4720["keyB-4720"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
