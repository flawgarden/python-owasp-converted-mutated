
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02223", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        params = request.args.to_dict()
        param = ""
        if params:
            param = params.get('BenchmarkTest02223', '')

        bar = do_something(param)

        response = app.response_class()
        response.headers['X-XSS-Protection'] = '0'
        response.set_data("Formatted like: {} and {}.".format("a", bar))
        return response

def do_something(param):
    return param + "_SafeStuff"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
