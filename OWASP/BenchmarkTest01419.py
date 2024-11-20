
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01419", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys() if request.method == 'GET' else request.form.keys()
    for name in names:
        values = request.args.getlist(name) if request.method == 'GET' else request.form.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest01419":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data("Formatted like: a and {}.".format(bar))
    return response

def do_something(param):
    # Simple if statement that assigns constant to bar on true condition
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
