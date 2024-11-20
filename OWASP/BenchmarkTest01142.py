
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01142", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Host', 'Connection', 'Accept-Encoding', 'Accept-Language']:
            continue  # If standard header, move on to next one
        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = Test().do_something(request, param)

    request.environ['werkzeug.session'].setdefault('userid', bar)

    response.set_data(f"Item: 'userid' with value: '{bar}' saved in session.")
    return response

class Test:
    def do_something(self, request, param):
        bar = ""

        # Simple if statement that assigns constant to bar on true condition
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
