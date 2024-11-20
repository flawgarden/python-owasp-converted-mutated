
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02317", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.to_dict(flat=False)

    for name, values in names.items():
        if values:
            for value in values:
                if value == "BenchmarkTest02317":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    response = Response()
    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(bar % tuple(obj))
    response.content_type = "text/html;charset=UTF-8"
    return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
