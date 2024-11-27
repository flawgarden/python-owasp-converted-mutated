
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01711", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01711="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01711' in query string."

    param = query_string[param_loc + len(paramval):]  # assume last parameter in query string
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval): ampersand_loc]

    param = param # No need for decoding, Flask handles it internally

    bar = Test().do_something(request, param)

    # Simulating session storage in Flask
    request.environ['werkzeug.request'].session['userid'] = bar

    return "Item: 'userid' with value: '{}' saved in session.".format(bar)

class Test:
    def do_something(self, request, param):
        bar = ""
        num = 196

        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
