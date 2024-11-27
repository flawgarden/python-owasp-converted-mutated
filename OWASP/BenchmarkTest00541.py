
from flask import Flask, request, make_response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00541", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00541":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = f"{bar.format(*obj)}"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
