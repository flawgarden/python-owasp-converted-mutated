
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02681", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.args.get("BenchmarkTest02681")
        bar = do_something(param)

        response = app.response_class(
            response=bar,
            status=200,
            mimetype='text/html'
        )
        response.headers['X-XSS-Protection'] = '0'
        return response
    return render_template("index.html")

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
