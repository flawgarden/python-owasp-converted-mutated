
import base64
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-02/BenchmarkTest01181", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.headers.get('Referer', '')

        param = param.encode('utf-8').decode('utf-8')

        bar = Test().do_something(param)

        response.headers['X-XSS-Protection'] = '0'
        response.set_data(bar)
        return response


class Test:

    def do_something(self, param):
        bar = ''
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
