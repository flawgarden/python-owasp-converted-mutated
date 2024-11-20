
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01692", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest01692="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01692' in query string."

    param = query_string[param_loc + len(paramval):]  
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = base64.urlsafe_b64decode(param).decode("utf-8")

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == "nt":  
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        result = process.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        a28453 = param  
        b28453 = a28453 + " SafeStuff"  
        b28453 = b28453[:-1] + "Chars"  
        
        map28453 = {}
        map28453["key28453"] = b28453   
        c28453 = map28453["key28453"]  
        d28453 = c28453[:-1]  
        e28453 = base64.b64decode(base64.b64encode(d28453.encode())).decode()  
        f28453 = e28453.split(" ")[0]  
        
        thing = create_thing()
        g28453 = "barbarians_at_the_gate"  
        bar = thing.do_something(g28453)  

        return bar

def create_thing():
    class ThingInterface:
        def do_something(self, input_str):
            return f"Processed {input_str}"
    
    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
