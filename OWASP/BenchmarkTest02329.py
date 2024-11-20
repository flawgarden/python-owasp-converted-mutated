
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02329", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")
    param = ""
    flag = True

    for name in request.args.keys():
        if flag:
            values = request.args.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest02329":
                        param = name
                        flag = False

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    if bar is not None:
        response.data = bar

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
