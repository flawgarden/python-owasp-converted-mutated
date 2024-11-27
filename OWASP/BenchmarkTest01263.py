
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-02/BenchmarkTest01263", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)


def benchmark_test_post(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest01263", "")

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = ''.join(bar)
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
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar


if __name__ == '__main__':
    app.run(host='0.0.0.0')
