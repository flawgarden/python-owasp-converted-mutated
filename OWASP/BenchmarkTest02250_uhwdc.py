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

from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02250", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02250', '')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # For Windows
        cmd = "echo "

    try:
        gen = simple_generator(bar, 0.34498445776085307, 0.9594420375534948)
        genToList = list(gen)
        bar = genToList[1]
        process = subprocess.Popen(cmd + bar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return "<pre>" + output.decode() + "</pre>"
    except Exception as e:
        return "<pre>" + str(e) + "</pre>"

def do_something(param):
    bar = "safe!"
    map94176 = {
        "keyA-94176": "a-Value",
        "keyB-94176": param,
        "keyC": "another-Value"
    }
    bar = map94176["keyB-94176"]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
