
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01456", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01456":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    request.session['userid'] = bar

    return "Item: 'userid' with value: '" + bar + "' saved in session."

class Test:

    def do_something(self, request, param):
        # Simple if statement that assigns param to bar on true condition
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
