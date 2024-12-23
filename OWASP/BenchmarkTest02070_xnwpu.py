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
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02070", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = ""
    headers = request.headers.get('BenchmarkTest02070')

    if headers:
        a12341 = DerivedBinaryOpClass1()
        headers = a12341.virtual_call("", headers)
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(escape_for_html(str(e)))
        return response
    return response

def do_something(request, param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def get_insecure_os_command_string():
    # Placeholder for the method to get the insecure OS command string
    return "echo"

def escape_for_html(text):
    from html import escape
    return escape(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
