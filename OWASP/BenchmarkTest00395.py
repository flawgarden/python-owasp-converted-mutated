
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00395", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.form.get('BenchmarkTest00395', "")
        bar = ""
        if param:
            bar = param.split(" ")[0]

        response.headers['X-XSS-Protection'] = '0'
        length = 1
        if bar:
            length = len(bar)
            response.data = bar[:length]
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
