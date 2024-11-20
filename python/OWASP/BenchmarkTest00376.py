
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00376", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00376', '')
    
    bar = param
    
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data("Formatted like: {} and {}.".format("a", bar))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
