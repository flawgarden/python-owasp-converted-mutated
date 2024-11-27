
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00284", methods=['GET', 'POST'])
def benchmark_test():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer  # just grab first element

    # URL Decode the header value
    param = param.encode('utf-8').decode('utf-8')

    bar = param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
