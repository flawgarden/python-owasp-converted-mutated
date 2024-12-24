from queue import SimpleQueue, Queue, PriorityQueue
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

@app.route("/pathtraver-00/BenchmarkTest00045", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return render_template("index.html")

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    values = request.args.getlist("BenchmarkTest00045")
    param = values[0] if values else ""

    file_name = os.path.join('testfiles', param)
    queue787231 = PriorityQueue()
    queue787231.put(file_name)
    queue787231.get()
    file_name = queue787231.get_nowait()

    try:
        with open(file_name, 'w') as fos:
            fos.write("Now ready to write to file: " + file_name)
            response.set_data("Now ready to write to file: " + file_name)

    except Exception as e:
        print("Couldn't open FileOutputStream on file: '" + file_name + "'")

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
