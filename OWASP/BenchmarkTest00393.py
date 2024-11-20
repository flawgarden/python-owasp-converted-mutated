
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-00/BenchmarkTest00393", methods=['GET', 'POST'])
def benchmark_test00393():
    if request.method == 'GET':
        return benchmark_test00393_post()
    return benchmark_test00393_post()


def benchmark_test00393_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest00393', "")
    bar = ""

    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
