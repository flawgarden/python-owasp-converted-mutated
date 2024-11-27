
import os
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00392", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00392', '')
    
    bar = param
    if param and len(param) > 1:
        sbxyz38384 = list(param)
        bar = ''.join(sbxyz38384[:-1] + ['Z'])

    response = make_response(bar)
    response.headers["X-XSS-Protection"] = "0"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
