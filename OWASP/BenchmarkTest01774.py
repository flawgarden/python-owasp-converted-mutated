
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01774", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest01774", "")
    
    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-58318": "a_Value",
            "keyB-58318": param,
            "keyC": "another_Value"
        }
        bar = map_.get("keyB-58318")
        bar = map_.get("keyA-58318")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
