
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02330", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.values.keys()
    for name in names:
        values = request.values.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02330":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar:
        length = len(bar)
        response.set_data(bar[:length])

    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
