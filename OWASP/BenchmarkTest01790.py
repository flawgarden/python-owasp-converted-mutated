
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01790", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.args.get("BenchmarkTest01790", "")
        bar = Test().do_something(param)
        response = f"Parameter value: {bar}"
        return response, {'X-XSS-Protection': '0'}

class Test:
    @staticmethod
    def do_something(param):
        from html import escape
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
