
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01551", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()

    param = request.args.get("BenchmarkTest01551", "")
    bar = Test().do_something(param)

    # Save 'userid' in session
    request.session['userid'] = bar

    response.data = f"Item: 'userid' with value: '{Utils.encode_for_html(bar)}' saved in session."
    response.content_type = "text/html;charset=UTF-8"
    return response

class Test:

    def do_something(self, param):
        sbxyz68516 = str(param)
        bar = sbxyz68516 + "_SafeStuff"
        return bar

class Utils:

    @staticmethod
    def encode_for_html(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
