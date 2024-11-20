
from flask import Flask, request, render_template
import urllib.parse
from html import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00325", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if 'BenchmarkTest00325' in request.headers:
        param = request.headers['BenchmarkTest00325']  # just grab first element

    param = urllib.parse.unquote(param)

    bar = escape(param)

    request.session['userid'] = bar

    return f"Item: 'userid' with value: '{escape(bar)}' saved in session."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
