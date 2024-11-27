
from flask import Flask, request, make_response
from urllib.parse import quote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00648", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.args.get("BenchmarkTest00648", "")
        bar = quote(param, safe="")
        
        response = make_response(bar)
        response.headers['X-XSS-Protection'] = '0'
        return response
    elif request.method == 'GET':
        return benchmark_test()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
