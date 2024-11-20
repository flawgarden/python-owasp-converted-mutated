
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00892", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.args.get('BenchmarkTest00892', '')
    bar = param

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar:
        length = len(bar)
        response.data = bar.encode('utf-8')[:length]
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
