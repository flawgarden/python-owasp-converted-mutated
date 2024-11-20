
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02225", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02225', '')

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(response.get_data(as_text=True).format(bar, "a", "b"))
    return response

def do_something(param):
    bar = "safe!"
    map73885 = {
        "keyA-73885": "a-Value",
        "keyB-73885": param,
        "keyC": "another-Value"
    }
    bar = map73885["keyB-73885"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
