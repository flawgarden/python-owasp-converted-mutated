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

from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01050", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('Referer', '')
    gen = infinite_gen(param, "eezqh")
    genToList = [next(gen) for _ in range(1000)]
    param = genToList[1000]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response = make_response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:
    def do_something(self, request, param):
        sbxyz75528 = str(param)
        bar = sbxyz75528 + "_SafeStuff"
        return bar

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
