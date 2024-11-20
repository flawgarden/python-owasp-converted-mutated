
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02712", methods=['GET', 'POST'])
def benchmark_test_02712():
    if request.method == 'POST':
        return do_post(request)
    return do_get()

def do_get():
    return do_post(request)

def do_post(request):
    response = "text/html;charset=UTF-8"
    param = request.values.get("BenchmarkTest02712", '')

    bar = do_something(request, param)

    return f"Parameter value: {bar}", 200, {'Content-Type': response, 'X-XSS-Protection': '0'}

def do_something(request, param):
    bar = "safe!"
    map52216 = {}
    map52216["keyA-52216"] = "a_Value"
    map52216["keyB-52216"] = param
    map52216["keyC"] = "another_Value"
    bar = map52216.get("keyB-52216")
    bar = map52216.get("keyA-52216")

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
