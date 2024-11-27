
from flask import Flask, request, make_response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00588", methods=['GET', 'POST'])
def benchmark_test_00588():
    if request.method == 'GET':
        return benchmark_test_00588_post()
    return benchmark_test_00588_post()

def benchmark_test_00588_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00588":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    # Set session attribute
    request.environ['werkzeug.session'].set(bar, "10340")

    response_text = f"Item: '{html.escape(bar)}' with value: '10340' saved in session."
    return make_response(response_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
