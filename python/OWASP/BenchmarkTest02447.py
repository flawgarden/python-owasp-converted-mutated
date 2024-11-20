
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02447", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_text = "Item: 'userid' with value: '"
    
    param = request.args.get("BenchmarkTest02447", "")
    bar = do_something(param)
    
    # Simulating session storage
    request.environ['werkzeug.session'].setdefault('userid', bar)

    response_text += escape_html(bar) + "' saved in session."
    return response_text

def do_something(param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

def escape_html(text):
    from markupsafe import escape
    return escape(text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
