
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00727", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        values = request.values.getlist("BenchmarkTest00727")
        param = values[0] if values else ""

        bar = param
        if param and len(param) > 1:
            bar = param[:-1]

        response.headers['X-XSS-Protection'] = '0'
        response.set_data(bar)
        return response
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
