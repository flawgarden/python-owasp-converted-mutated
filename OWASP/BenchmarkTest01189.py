
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01189", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ''
    if 'BenchmarkTest01189' in request.headers:
        param = request.headers['BenchmarkTest01189']  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = ''
    a1 = ''
    a2 = ''
    args = []
    os_name = os.name

    if os_name == 'nt':
        a1 = 'cmd.exe'
        a2 = '/c'
        cmd = "echo"
        args = [a1, a2, cmd + ' ' + bar]
    else:
        a1 = 'sh'
        a2 = '-c'
        cmd = "ping -c1 "
        args = [a1, a2, cmd + bar]

    try:
        p = os.popen(' '.join(args))
        result = p.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:

    def do_something(self, request, param):
        bar = ''

        # Simple if statement that assigns constant to bar on true condition
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
