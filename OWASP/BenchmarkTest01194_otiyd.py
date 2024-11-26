#Snyk original results: [78]
#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Snyk analysis results: [79, 78]
#Bearer analysis results: []
#CodeQL analysis results: [563, 78, 88]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01194.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/comprehension.tmt with name nested_list_comprehension_positive
#Used extensions:
#Program:
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


@app.route("/cmdi-01/BenchmarkTest01194", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = ""
    headers = request.headers.get('BenchmarkTest01194')

    if headers:
        param = headers  # just grab first element
        tmpList = [[param], ["nqaow"], ["paiga"]]
        compList = [x for x in tmpList]
        param = compList[0][0]

    param = param  # URL Decode the header value

    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Assuming platform-specific command

    args_env = ["Foo=bar"]
    try:
        p = os.popen(cmd + bar)
        output = p.read()
        response.set_data(output)

    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

    return response


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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
