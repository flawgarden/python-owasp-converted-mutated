
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01260", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get('BenchmarkTest01260', '')
    bar = Test().do_something(param)

    response = app.response_class(
        response="",
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    response.set_data(f"Formatted like: {bar} and b.")
    return response

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
