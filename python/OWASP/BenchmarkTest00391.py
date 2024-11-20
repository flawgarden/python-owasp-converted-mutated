
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-00/BenchmarkTest00391", methods=['GET', 'POST'])
def benchmark_test00391():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get('BenchmarkTest00391', '')
        bar = escape(param)

        response = app.response_class(
            response=bar,
            status=200,
            mimetype='text/html'
        )
        response.headers['X-XSS-Protection'] = '0'
        return response


def escape(string):
    return string.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#x27;')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
