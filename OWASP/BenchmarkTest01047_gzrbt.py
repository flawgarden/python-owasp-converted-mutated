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
    duck_like = Duck()
    response = make_it_quack_attr(duck_like, response)
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

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck, arg):
    if hasattr(duck, 'quack'):
        return duck.quack(arg)
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
