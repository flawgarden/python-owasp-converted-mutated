
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-03/BenchmarkTest01591", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)


def benchmark_test_post(request):
    response = app.response_class(
        content_type='text/html;charset=UTF-8'
    )

    values = request.args.getlist("BenchmarkTest01591")
    param = values[0] if values else ""

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    return response


def do_something(request, param):
    a1207 = param  # assign
    b1207 = a1207 + " SafeStuff"  # append some safe content
    b1207 = b1207[:-5] + "Chars"  # replace some of the end content
    map1207 = {'key1207': b1207}  # put in a collection
    c1207 = map1207['key1207']  # get it back out
    d1207 = c1207[:-1]  # extract most of it
    e1207 = base64.b64decode(base64.b64encode(d1207.encode())).decode()  # B64 encode and decode it
    f1207 = e1207.split(" ")[0]  # split it on a space
    g1207 = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
    bar = do_something_reflection(g1207)  # reflection

    return bar


def do_something_reflection(input_str):
    return f"Processed: {input_str}"  # Placeholder for the actual functionality


if __name__ == "__main__":
    app.run(host='0.0.0.0')
