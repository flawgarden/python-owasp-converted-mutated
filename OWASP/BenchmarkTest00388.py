
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00388", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00388', '')
    sbxyz30382 = str(param)
    bar = sbxyz30382 + "_SafeStuff"
    
    response = app.response_class(
        response=bar,
        status=200,
        content_type='text/html;charset=UTF-8'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
