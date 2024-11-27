
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01615", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist("BenchmarkTest01615")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        request.environ['wsgi.session'][bar] = "10340"

        return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            sbxyz57216 = list(param)
            sbxyz57216[-1] = 'Z'
            bar = ''.join(sbxyz57216)

        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
