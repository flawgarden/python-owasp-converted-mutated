
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02509", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_post(request)

def do_post(request):
    response = app.response_class(content_type="text/html;charset=UTF-8")

    values = request.values.getlist("BenchmarkTest02509")
    param = values[0] if values else ""

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = f"Parameter value: {bar}"
    return response

def do_something(request, param):
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
