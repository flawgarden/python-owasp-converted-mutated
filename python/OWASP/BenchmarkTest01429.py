
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01429", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest01429":
                    param = name
                    flag = False

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ('C', 'D'):
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
