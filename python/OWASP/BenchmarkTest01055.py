
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01055", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("Referer", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response = app.response_class(response=bar, status=200)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
