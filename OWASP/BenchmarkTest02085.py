
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02085", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if "BenchmarkTest02085" in request.headers:
        param = request.headers["BenchmarkTest02085"]

    param = param  # No need for URL decoding, Flask does it automatically

    bar = do_something(request, param)

    # Simulating the session attribute
    request.environ['werkzeug.session'] = {}
    request.environ['werkzeug.session']['userid'] = bar

    response.data = (
        f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."
    ).encode('utf-8')

    return response

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def encode_for_html(value):
    from html import escape
    return escape(value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
