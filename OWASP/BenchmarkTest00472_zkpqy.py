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

from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00472", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00472', '')
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    queue787231 = Queue()
    queue787231.put_nowait(bar)
    queue787231.get()
    bar = queue787231.get_nowait()

    response = app.response_class(
        response='Formatted like: %s and %s.' % (bar, "b"),
        status=200,
        mimetype='text/html'
    )
    response.headers["X-XSS-Protection"] = "0"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
