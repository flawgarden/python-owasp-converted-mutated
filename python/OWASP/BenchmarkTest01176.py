
import urllib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01176", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = ""
    headers = request.headers.get("Referer")

    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response = "X-XSS-Protection: 0"
    obj = ("a", bar)
    output = "Formatted like: %s and %s." % obj
    return output  # This would be the response output

class Test:

    def do_something(self, request, param):
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        # Simple case statement that assigns param to bar on conditions 'A', 'C', or 'D'
        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
