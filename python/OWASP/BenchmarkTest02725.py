
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02725", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response_content_type = "text/html;charset=UTF-8"
        param = request.args.get('BenchmarkTest02725')

        bar = do_something(param)

        # Store in session
        request.environ['werkzeug.session'].set('userid', bar)

        return "Item: 'userid' with value: '{}' saved in session.".format(bar)

def do_something(param):
    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
