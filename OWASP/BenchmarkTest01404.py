
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01404", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01404":
                    param = name
                    flag = False
        if not flag:
            break

    bar = Test().do_something(request, param)

    file_target = os.path.join(bar, "Test.txt")
    output = f"Access to file: '{file_target}' created.\n"
    if os.path.exists(file_target):
        output += " And file already exists.\n"
    else:
        output += " But file doesn't exist yet.\n"

    return output

class Test:
    def do_something(self, request, param):
        a75056 = param 
        b75056 = a75056 + " SafeStuff"
        b75056 = b75056[:-len("Chars")] + "Chars"
        map75056 = {'key75056': b75056}
        c75056 = map75056["key75056"]
        d75056 = c75056[:-1]
        
        e75056 = base64.b64decode(base64.b64encode(d75056.encode())).decode()
        f75056 = e75056.split(" ")[0]
        
        thing = create_thing()
        g75056 = "barbarians_at_the_gate"
        bar = thing.do_something(g75056)

        return bar

def create_thing():
    class ThingInterface:
        def do_something(self, data):
            return "/some/path/" + data
            
    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
