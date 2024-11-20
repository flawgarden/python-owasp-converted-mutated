
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02122", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02122', '')
    bar = do_something(param)

    response = Response()
    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.data = f"<!DOCTYPE html>\n<html>\n<body>\n<p>Formatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>"
    response.content_type = "text/html;charset=UTF-8"
    
    return response

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
