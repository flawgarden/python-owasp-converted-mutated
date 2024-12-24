from Record import *
from Exceptions import *
from Concurrency import *
from Imports import *
from ClassWrappers import *
from MonkeyClass import *
from MagicClass import *
from UnaryOpInterface import *
from BinaryOpInterface import *
from DerivedBinaryOpClass import *
from BaseBinaryOpClass import *
from UnaryOpClass import *
from ImplBinaryOpInterfaceClass import *
from Duck import *
from ReflectionHelper import *
from StringHolder import *
from StringFactory import *
from InstanceInitializer import *
from NestedStringHolder import *
from ArrayHolder import *
from NestedFields import *
from StaticFieldHolder import *
from UnaryOpMutationInterface import *
from GenericClass import *
from SuperInterface import *
from SuperClass import *

import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01066", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_content_type = "text/html;charset=UTF-8"
    param = request.headers.get("BenchmarkTest01066", "")

    param = base64.b64decode(base64.b64encode(param.encode())).decode()

    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(f"{cmd} {bar}")  # Execute command
        output = process.read()
        return output
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {e}"

class Test:
    def do_something(self, param):
        first = SimpleRecord(param)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        param = nested.a.t
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

def get_insecure_os_command_string():
    return "echo"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
