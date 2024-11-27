
from flask import Flask, request, session, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02263", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02263", "")
        bar = do_something(param)

        session[bar] = "10340"

        return f"Item: '{encode_for_html(bar)}' with value: '10340' saved in session."
    return render_template("index.html")

def do_something(param):
    bar = param
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
