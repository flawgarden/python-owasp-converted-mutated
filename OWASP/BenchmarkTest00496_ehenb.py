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
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00496", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = "<html><body>"
    param = request.args.get('BenchmarkTest00496', '')

    bar = ""
    arr4124 = ["wdodr"]
    nested7231 = NestedFields1(initialValues=arr4124)
    param = nested7231.nested1.values[0]
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        results = process.read()
        response += results
        process.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += str(e)

    response += "</body></html>"
    return response

def get_insecure_os_command_string():
    return "echo"  # Example command; adjust as necessary

if __name__ == "__main__":
    app.run(host='0.0.0.0')
