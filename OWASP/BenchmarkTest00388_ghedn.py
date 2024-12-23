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

from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00388", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00388', '')
    sbxyz30382 = str(param)
    duck_like = NotADuck()
    sbxyz30382 = make_it_quack(duck_like, sbxyz30382)
    bar = sbxyz30382 + "_SafeStuff"

    response = app.response_class(
        response=bar,
        status=200,
        content_type='text/html;charset=UTF-8'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

if __name__ == '__main__':
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
