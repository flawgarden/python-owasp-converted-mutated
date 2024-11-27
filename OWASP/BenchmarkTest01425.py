
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01425", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()  # Use request.args for GET parameters
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01425":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    response = app.response_class()
    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target == 'C' or switch_target == 'D':
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
