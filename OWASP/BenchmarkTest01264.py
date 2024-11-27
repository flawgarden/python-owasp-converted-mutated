
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01264", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest01264', '')
    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

class Test:

    def do_something(self, request, param):
        # Simulating encoding to prevent XSS
        bar = param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
