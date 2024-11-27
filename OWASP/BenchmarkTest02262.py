
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02262", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.args.get('BenchmarkTest02262', '')

        bar = do_something(param)

        # Simulate storing the value in session
        request.environ['werkzeug.session'].update({'userid': bar})

        return "Item: 'userid' with value: '{}' saved in session.".format(bar)

def do_something(param):
    bar = escape_html(param)
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
