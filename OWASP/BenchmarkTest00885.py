
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00885", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response(content_type="text/html;charset=UTF-8")

        param = request.args.get("BenchmarkTest00885")
        bar = param
        if param and len(param) > 1:
            sbxyz28240 = list(param)
            bar = ''.join(sbxyz28240[:-1]) + 'Z'

        response.headers['X-XSS-Protection'] = '0'
        obj = ["a", "b"]
        response.data = f"{bar % obj}"

        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
