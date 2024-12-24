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
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01944", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    if request.headers.get("BenchmarkTest01944") is not None:
        param = request.headers.get("BenchmarkTest01944")

    param = param.encode('utf-8').decode('unicode_escape')
    try:
        a = 1 / 0
    except ZeroDivisionError as e:
        param = ""

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo"

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output.encode('utf-8')
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e).encode('utf-8')
        return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
