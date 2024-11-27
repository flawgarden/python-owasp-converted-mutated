
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02723", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    param = request.args.get('BenchmarkTest02723')
    bar = do_something(param)

    # Simulating session storage (using Flask's session)
    from flask import session
    session[bar] = "10340"

    response.data = f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."
    response.content_type = "text/html;charset=UTF-8"
    return response

def do_something(param):
    sbxyz51151 = str(param)
    bar = sbxyz51151 + "_SafeStuff"
    return bar

def encode_for_html(input):
    from markupsafe import escape
    return escape(input)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
