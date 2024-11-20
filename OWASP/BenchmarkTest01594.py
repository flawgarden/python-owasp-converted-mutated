
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01594", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist('BenchmarkTest01594')
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        response = app.response_class()
        response.headers['X-XSS-Protection'] = '0'
        response.data = bar
        response.mimetype = 'text/html'
        return response
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        sbxyz51154 = str(param)
        bar = sbxyz51154 + "_SafeStuff"
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
