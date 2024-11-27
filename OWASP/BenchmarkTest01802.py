
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01802", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.form.get("BenchmarkTest01802", None)

        bar = Test().do_something(request, param)

        request.environ['werkzeug.session'][bar] = "10340"

        response.set_data(
            f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."
        )
        return response
    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
