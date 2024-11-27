
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02688", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02688", "")
        bar = do_something(param)
        response = app.response_class()
        response.headers["X-XSS-Protection"] = "0"
        response.set_data(bar)
        return response
    return render_template("index.html")

def do_something(param):
    bar = escape_html(param)
    return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
