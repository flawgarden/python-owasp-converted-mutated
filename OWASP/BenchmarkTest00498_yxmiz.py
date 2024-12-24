from queue import SimpleQueue, Queue, PriorityQueue
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
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00498", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.values.get('BenchmarkTest00498', '')
    queue787231 = Queue()
    queue787231.put_nowait(param)
    param = queue787231.get()

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = 'your_insecure_command_here'  # Replace with actual method to get the command
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = p.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
