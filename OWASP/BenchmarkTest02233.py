
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02233", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get('BenchmarkTest02233', '')
    bar = do_something(request, param)
    response.headers['X-XSS-Protection'] = '0'
    response.data = f"{bar} %s %s" % ("a", "b")
    return response

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
