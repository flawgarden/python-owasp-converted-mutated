
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01261", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01261", "")
    bar = Test().do_something(request, param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    response.content_type = "text/html;charset=UTF-8"
    return response

class Test:
    def do_something(self, request, param):
        a34194 = param
        b34194 = str(a34194)
        b34194 += " SafeStuff"
        b34194 = b34194[:-len("Chars")] + "Chars"

        map34194 = {"key34194": b34194}
        c34194 = map34194["key34194"]
        d34194 = c34194[:-1]

        e34194 = base64.b64decode(base64.b64encode(d34194.encode())).decode()
        f34194 = e34194.split(" ")[0]

        # Replace ThingInterface with an appropriate class or method call
        bar = something_with(f34194)
        return bar

def something_with(value):
    # Simulated reflection call
    return f"Processed: {value}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
