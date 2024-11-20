
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02403", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)

def do_get(request):
    return do_post(request)

def do_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get("BenchmarkTest02403", "")
    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response

def do_something(request, param):
    a34270 = param
    b34270 = a34270 + " SafeStuff"
    b34270 = b34270[:-len("Chars")] + "Chars"
    map34270 = {"key34270": b34270}
    c34270 = map34270["key34270"]
    d34270 = c34270[:-1]
    e34270 = base64.b64decode(base64.b64encode(d34270.encode())).decode()
    f34270 = e34270.split(" ")[0]
    thing = create_thing()
    bar = thing.do_something(f34270)

    return bar

def create_thing():
    return Thing()

class Thing:
    def do_something(self, input):
        return f"Processed: {input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
