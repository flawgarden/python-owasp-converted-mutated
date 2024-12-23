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

from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest01047", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'Referer' in request.headers:
        param = request.headers['Referer']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.set_data("<!DOCTYPE html>\n<html>\n<body>\n<p>{}</p>\n</body>\n</html>".format(
        "Formatted like: {} and {}.".format(*obj)
    ))

    return response

class Test:
    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            sbxyz50709 = list(param)
            sbxyz50709[-1] = 'Z'
            bar = ''.join(sbxyz50709)
        arr4124 = ["lexzx"]
        nested7231 = NestedFields1(initialValues=arr4124)
        bar = nested7231.nested1.values[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
