
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00555", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00555":
                    param = name
                    flag = False
                    break

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar.encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
