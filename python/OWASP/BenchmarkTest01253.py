
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01253", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01253", "")
        bar = Test().do_something(request, param)

        response = app.response_class()
        response.headers["X-XSS-Protection"] = "0"
        response.set_data(bar % ("a", "b"))
        return response
    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map15481 = {"keyA-15481": "a-Value", "keyB-15481": param, "keyC": "another-Value"}
        bar = map15481["keyB-15481"]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
