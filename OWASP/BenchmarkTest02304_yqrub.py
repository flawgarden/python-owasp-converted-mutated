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

@app.route("/pathtraver-02/BenchmarkTest02304", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02304":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join('testfiles', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response = "The beginning of file: '{}' is:\n\n".format(file_name)
            response += b.decode('utf-8', errors='ignore')
            return response
    except Exception as e:
        print("Couldn't open FileInputStream on file: '{}'".format(file_name))
    return "Error opening file."

def do_something(param):
    set787231 = set()
    set787231.add(param)
    set787231.add(param)
    set787231.remove(param)
    param = next(iter(set787231))
    bar = ""
    if param is not None:
        values_list = ['safe', param, 'moresafe']
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
