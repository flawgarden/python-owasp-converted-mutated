
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02325", methods=['GET', 'POST'])
def benchmark_test_02325():
    if request.method == 'GET':
        return benchmark_test_02325()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")
    
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02325":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
