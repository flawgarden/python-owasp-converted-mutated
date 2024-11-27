
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01338", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return process_request()
    return process_request()

def process_request():
    param = request.args.get('BenchmarkTest01338', '')
    bar = Test().do_something(param)

    response = app.response_class(
        response=bar,
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
