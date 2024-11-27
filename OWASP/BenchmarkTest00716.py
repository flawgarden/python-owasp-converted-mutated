
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00716", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = "text/html;charset=UTF-8"

        param = request.values.get('BenchmarkTest00716', '')

        bar = param  # Replace with appropriate HTML encoding function if needed

        response.headers['X-XSS-Protection'] = "0"
        response.data = "Formatted like: {} and {}.".format("a", bar)
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
