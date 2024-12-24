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

@app.route("/xss-00/BenchmarkTest00290", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer
    s123 = SimpleImportFrom()
    param = s123.func("mlvne")

    param = urllib.parse.unquote(param)

    sbxyz73567 = param + "_SafeStuff"
    response = make_response(sbxyz73567)
    response.headers['X-XSS-Protection'] = '0'

    return response

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
