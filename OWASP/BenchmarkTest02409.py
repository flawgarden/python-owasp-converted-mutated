
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02409", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    param = request.args.get("BenchmarkTest02409", "")
    bar = do_something(param)

    response = Response(bar, content_type="text/html;charset=UTF-8")
    response.headers["X-XSS-Protection"] = "0"
    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
