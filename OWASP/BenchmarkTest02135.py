
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02135", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get("BenchmarkTest02135", "")
    bar = do_something(request, param)

    response = app.response_class()
    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    response.mimetype = 'text/html;charset=UTF-8'
    return response

def do_something(request, param):
    a95930 = param
    b95930 = str(a95930) + " SafeStuff"
    b95930 = b95930[:-5] + "Chars"
    map95930 = {'key95930': b95930}
    c95930 = map95930['key95930']
    d95930 = c95930[:-1]
    e95930 = base64.b64decode(base64.b64encode(d95930.encode())).decode()
    f95930 = e95930.split(" ")[0]
    g95930 = "barbarians_at_the_gate"
    bar = g95930  # Placeholder for reflection action with the static value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
