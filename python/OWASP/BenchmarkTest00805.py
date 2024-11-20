
import urllib.parse
from flask import Flask, request, Response
from flask import render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00805", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00805="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return Response("getQueryString() couldn't find expected parameter 'BenchmarkTest00805' in query string.", status=400)

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    a72616 = param
    b72616 = str(a72616)
    b72616 += " SafeStuff"
    b72616 = b72616[:-5] + "Chars"
    map72616 = {'key72616': b72616}
    c72616 = map72616['key72616']
    d72616 = c72616[:-1]
    e72616 = base64.b64decode(base64.b64encode(d72616.encode())).decode()
    f72616 = e72616.split(" ")[0]

    # Assuming that `ThingInterface` and `ThingFactory` are defined elsewhere
    thing = create_thing()
    bar = thing.doSomething(f72616)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def create_thing():
    class ThingInterface:
        def doSomething(self, value):
            return f"Processed: {value}"

    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
