
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00549", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest00549":
                    param = name
                    flag = False

    bar = ""
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    response.headers["X-XSS-Protection"] = "0"
    response.data = ''.join(bar).encode('utf-8')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
