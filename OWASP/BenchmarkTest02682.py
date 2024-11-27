
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/xss-05/BenchmarkTest02682", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02682")
    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
