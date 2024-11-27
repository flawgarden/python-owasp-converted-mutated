
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02328", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02328":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    length = 1
    if bar is not None:
        length = len(bar)
        response.set_data(bar)

    return response

def do_something(request, param):
    bar = param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
