
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01958", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01958", "")

    param = param  # URL decoding is handled by Flask automatically

    bar = do_something(request, param)

    # Simulate saving to session
    request.environ['werkzeug.session'].data['userid'] = bar

    response.set_data(
        "Item: 'userid' with value: '"
        + encode_for_html(bar)
        + "' saved in session."
    )
    response.content_type = "text/html;charset=UTF-8"
    return response

def do_something(request, param):
    bar = param
    if param and len(param) > 1:
        sbxyz15757 = list(param)
        sbxyz15757[-1] = 'Z'
        bar = ''.join(sbxyz15757)
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
