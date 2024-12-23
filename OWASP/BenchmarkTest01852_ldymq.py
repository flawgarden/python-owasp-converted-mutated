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
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-02/BenchmarkTest01852", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("BenchmarkTest01852.html"))
        user_cookie = ('BenchmarkTest01852', 'ECHOOO', 60 * 3, request.path, request.host)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], path=user_cookie[3], secure=True)
        return response

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01852' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01852'])

        bar = do_something(param)

        a1, a2 = ("cmd.exe", "/c") if "Windows" in os.sys.platform else ("sh", "-c")
        args = [a1, a2, "echo " + bar]

        try:
            p = os.popen(' '.join(args))
            output = p.read()
            return output
        except Exception as e:
            print("Problem executing command")
            raise e


def do_something(param):
    num = 106
    nested7231 = NestedFields2("babhj")
    param = nested7231.nested1.nested1.value
    return "This should never happen" if (7 * 42) - num > 200 else param


if __name__ == "__main__":
    app.run(host='0.0.0.0')
