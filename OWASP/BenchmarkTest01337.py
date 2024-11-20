
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01337", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if request.args:
        param = request.args.get('BenchmarkTest01337', '')

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    response.response = f"{bar.format('a', 'b')}"
    return response

class Test:
    def do_something(self, request, param):
        sbxyz24804 = str(param)
        bar = sbxyz24804 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
