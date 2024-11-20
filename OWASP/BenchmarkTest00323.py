
import urllib.parse
from flask import Flask, request, session, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key_here'

@app.route("/trustbound-00/BenchmarkTest00323", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    headers = request.headers.getlist("BenchmarkTest00323")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    session['userid'] = bar

    return "Item: 'userid' with value: '{}' saved in session.".format(urllib.parse.quote_plus(bar))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
