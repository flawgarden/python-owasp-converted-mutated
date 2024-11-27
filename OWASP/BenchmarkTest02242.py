
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02242", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02242', '')

    bar = do_something(param)

    arg_list = []

    os_name = os.name
    if os_name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")
    
    arg_list.append("echo " + bar)

    process = os.popen(' '.join(arg_list))
    results = process.read()
    process.close()
    
    return results

def do_something(param):
    a91595 = param
    b91595 = a91595 + " SafeStuff"
    b91595 = b91595[:-5] + "Chars"

    map91595 = {}
    map91595["key91595"] = b91595
    c91595 = map91595["key91595"]
    d91595 = c91595[:-1]

    e91595 = base64.b64decode(base64.b64encode(d91595.encode())).decode()
    f91595 = e91595.split(" ")[0]

    thing = create_thing()
    g91595 = "barbarians_at_the_gate"
    bar = thing.do_something(g91595)

    return bar

class ThingInterface:
    def do_something(self, data):
        return "Reflection test successful: " + data

def create_thing():
    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
