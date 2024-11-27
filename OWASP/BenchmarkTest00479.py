
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00479", methods=['GET', 'POST'])
def benchmark_test_00479():
    if request.method == 'GET':
        return benchmark_test_00479_post()

    return benchmark_test_00479_post()

def benchmark_test_00479_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get('BenchmarkTest00479', '')

    bar = escape_html(param)

    response.headers['X-XSS-Protection'] = '0'
    if bar:
        response.set_data(bar)
    return response

def escape_html(s):
    if s is None:
        return ''
    return (s.replace('&', '&amp;')
             .replace('<', '&lt;')
             .replace('>', '&gt;')
             .replace('"', '&quot;')
             .replace("'", '&#x27;'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
