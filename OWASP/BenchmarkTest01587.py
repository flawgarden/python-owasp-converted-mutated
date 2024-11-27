
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01587", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.values.getlist("BenchmarkTest01587")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        response = app.response_class()
        response.headers["X-XSS-Protection"] = "0"
        response.set_data(bar % ("a", "b"))
        return response
    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
