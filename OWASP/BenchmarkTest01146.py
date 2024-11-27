
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01146", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ''
    names = request.headers.keys()
    for name in names:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection']:
            continue  # If standard header, move on to next one
        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = Test().do_something(request, param)
    request.environ['werkzeug.session'].user_id = bar

    return f"Item: 'userid' with value: '{bar}' saved in session."

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
