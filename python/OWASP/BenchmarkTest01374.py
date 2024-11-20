
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01374", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "Item saved in session."
    param = request.args.get('BenchmarkTest01374', '')

    bar = Test().do_something(param)

    # Simulating session storage
    request.environ['session'] = {bar: '10340'}

    return render_template("index.html", message=f"Item: '{bar}' with value: 10340 saved in session.")

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
