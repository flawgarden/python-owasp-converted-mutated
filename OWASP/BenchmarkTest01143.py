
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01143", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response="",
        status=200,
        mimetype='text/html'
    )

    param = ""
    for name in request.headers.keys():
        if name in ["User-Agent", "Accept", "Accept-Language", "Content-Type"]:  # Example common headers
            continue

        param = name
        break

    bar = Test().do_something(param)

    with request.session() as session:
        session['userid'] = bar

    response.set_data("Item: 'userid' with value: '" + bar + "' saved in session.")
    return response

class Test:

    def do_something(self, param):
        bar = f"{param}_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
