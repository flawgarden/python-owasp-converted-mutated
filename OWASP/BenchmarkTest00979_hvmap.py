#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [209, 78, 1004]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 614, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00979.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name nested_record_negative
#Used extensions:
#Program:
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00979", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00979.html"))
        user_cookie = make_response("", 200)
        user_cookie.set_cookie("BenchmarkTest00979", ".", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.headers.add('Set-Cookie', user_cookie.data)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00979' in the_cookies:
            param = the_cookies['BenchmarkTest00979']
        first = SimpleRecord(param)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        param = nested.b.t

        bar = Test().do_something(request, param)

        cmd = ""
        a1 = ""
        a2 = ""
        args = []
        os_name = os.name

        if os_name == 'nt':
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo "
            args = [a1, a2, cmd + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ls "
            args = [a1, a2, cmd + bar]

        args_env = {"foo": "bar"}

        try:
            process = os.popen(" ".join(args), 'r')
            output = process.read()
            return render_template("output.html", output=output)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", error_message=e)

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')