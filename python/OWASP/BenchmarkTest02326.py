
import base64
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02326", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02326":
                    param = name
                    flag = False
                    break
            if not flag:
                break

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

def do_something(param):
    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
