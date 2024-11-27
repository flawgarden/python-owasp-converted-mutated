
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00552", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True

    names = request.args.keys() if request.method == 'GET' else request.form.keys()
    for name in names:
        values = request.args.getlist(name) if request.method == 'GET' else request.form.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest00552":
                    param = name
                    flag = False

    bar = "safe!"
    map63597 = {
        "keyA-63597": "a-Value",
        "keyB-63597": param,
        "keyC": "another-Value"
    }
    bar = map63597.get("keyB-63597")

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
