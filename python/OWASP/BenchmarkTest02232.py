
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02232", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02232', '')
    
    bar = do_something(param)

    response = app.response_class()
    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar % ("a", "b"))
    response.content_type = "text/html;charset=UTF-8"
    return response

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
