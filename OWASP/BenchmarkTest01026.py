
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01026", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if request.headers.get("BenchmarkTest01026") is not None:
        param = request.headers.get("BenchmarkTest01026")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_target = os.path.join(bar)
    response.data = f"Access to file: '{file_target}' created."
    if os.path.exists(file_target):
        response.data += " And file already exists."
    else:
        response.data += " But file doesn't exist yet."
    
    return response

class Test:
    def do_something(self, request, param):
        a11433 = param
        b11433 = a11433 + " SafeStuff"
        b11433 = b11433[:-5] + "Chars"  # replace the end content
        map11433 = {}
        map11433["key11433"] = b11433
        c11433 = map11433["key11433"]
        d11433 = c11433[:-1]  
        e11433 = d11433.encode('utf-8').decode('utf-8') 
        f11433 = e11433.split(" ")[0]  
        thing = self.create_thing()
        g11433 = "barbarians_at_the_gate"
        bar = thing.do_something(g11433)

        return bar

    def create_thing(self):
        return ThingInterface()

class ThingInterface:
    def do_something(self, g11433):
        return f"/path/to/{g11433}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
