from GenericClass import *
from SuperClass import *
from SuperInterface import *
from BinaryOpInterface import *
from UnaryOpClass import *
from UnaryOpInterface import *
from ImplBinaryOpInterfaceClass import *
from BaseBinaryOpClass import *
from DerivedBinaryOpClass import *
from ArrayHolder import *
from StaticFieldHolder import *
from StringFactory import *
from NestedFields import *
from StringHolder import *
from NestedStringHolder import *
from InstanceInitializer import *
from Imports import *
from ReflectionHelper import *
from MagicClass import *
from Record import *
from UnaryOpMutationInterface import *
from MonkeyClass import *
from Exceptions import *
from ClassWrappers import *
from Concurrency import *
from Duck import *

import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01511", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest01511", "")
    bar = Test().do_something(request, param)
    response_headers = [("X-XSS-Protection", "0")]
    obj = [bar, "b"]
    return f"Formatted like: {obj[0]} and {obj[1]}.", response_headers

class Test:

    def do_something(self, request, param):
        bar = ""
        list787231 = []
        list787231.append(param)
        list1234 = []
        list1234.extend(list787231)
        param = list1234[-1]
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
