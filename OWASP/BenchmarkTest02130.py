
from flask import Flask, request, Response
import io

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02130", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")
    
    param = request.args.get('BenchmarkTest02130', "")
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = io.BytesIO(f"Formatted like: a and {bar}.".encode('utf-8')).getvalue()
    
    return response

def do_something(param):
    sbxyz60224 = str(param)
    bar = sbxyz60224 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
