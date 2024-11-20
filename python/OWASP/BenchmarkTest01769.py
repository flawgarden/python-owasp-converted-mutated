
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01769", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['X-XSS-Protection'] = '0'
    
    param = request.args.get("BenchmarkTest01769")

    bar = Test().do_something(param)

    obj = ["a", "b"]
    response.set_data(bar % obj)
    response.content_type = "text/html;charset=UTF-8"

    return response

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[1]  # get the last 'safe' value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
