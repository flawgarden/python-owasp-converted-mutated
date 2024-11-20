
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-00/BenchmarkTest00041", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response()
    response.headers['X-XSS-Protection'] = '0'
    param = request.args.get("BenchmarkTest00041", "")
    length = 1
    if param:
        length = len(param)
        response.data = param[:length].encode('utf-8')
    response.content_type = "text/html;charset=UTF-8"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
