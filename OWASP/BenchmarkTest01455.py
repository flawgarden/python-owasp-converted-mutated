
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01455", methods=['GET', 'POST'])
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
                if value == "BenchmarkTest01455":
                    param = name
                    flag = False

    bar = Test().do_something(param)

    # Simulating session storage
    request.environ['werkzeug.session'].update({'userid': bar})

    return f"Item: 'userid' with value: '{bar}' saved in session."

class Test:
    def do_something(self, param):
        bar = param
        if param is not None and len(param) > 1:
            bar = param[:-1]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
