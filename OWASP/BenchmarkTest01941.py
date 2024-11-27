
import os
from flask import Flask, request, render_template
import urllib.parse
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01941", methods=['GET', 'POST'])
def benchmark_test01941():
    if request.method == 'GET':
        return benchmark_test01941_post()
    return benchmark_test01941_post()

def benchmark_test01941_post():
    response_content_type = "text/html;charset=UTF-8"

    param = request.headers.get("BenchmarkTest01941", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    cmd = get_insecure_os_command_string()

    args_env = [bar]

    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        output = process.read()
        return output, response_content_type
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return escape_for_html(str(e)), response_content_type

def do_something(param):
    a20426 = param
    b20426 = a20426 + " SafeStuff"
    b20426 = b20426[:-5] + "Chars"

    map20426 = {}
    map20426["key20426"] = b20426
    c20426 = map20426["key20426"]
    d20426 = c20426[:-1]

    e20426 = base64.b64decode(base64.b64encode(d20426.encode())).decode()
    f20426 = e20426.split(" ")[0]

    thing = create_thing()
    g20426 = "barbarians_at_the_gate"
    bar = thing.do_something(g20426)

    return bar

def get_insecure_os_command_string():
    return "your_insecure_command_here"

def escape_for_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Implement this function to return an instance of your ThingInterface class
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
