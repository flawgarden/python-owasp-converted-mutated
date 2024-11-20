
import base64
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00717", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00717")
    param = values[0] if values else ""

    a59129 = param 
    b59129 = a59129 + " SafeStuff" 
    b59129 = b59129[:-5] + "Chars" 
    map59129 = {'key59129': b59129} 
    c59129 = map59129['key59129'] 
    d59129 = c59129[:-1] 
    e59129 = base64.b64decode(base64.b64encode(d59129.encode())).decode() 
    f59129 = e59129.split(" ")[0] 
    thing = create_thing()
    g59129 = "barbarians_at_the_gate" 
    bar = thing.do_something(g59129)

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"Formatted like: {f59129} and {bar}.".encode()

    return response

def create_thing():
    class ThingInterface:
        def do_something(self, val):
            return f"Processed: {val}"

    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
