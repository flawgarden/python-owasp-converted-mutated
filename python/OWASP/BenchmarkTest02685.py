
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02685", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post(request)
    return handle_get(request)

def handle_get(request):
    return handle_post(request)

def handle_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get("BenchmarkTest02685", None)

    bar = do_something(param)
    
    response.headers["X-XSS-Protection"] = "0"
    response.set_data(f"Formatted like: a and {bar}.")
    return response

def do_something(param):
    bar = ""
    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
