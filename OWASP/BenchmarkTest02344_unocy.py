#Snyk original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#CodeQL original results: []
#Semgrep original results: []
#-------------
#Bearer analysis results: [79]
#Snyk analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02344.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name nested_unary_lambda_mutation_positive
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
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02344", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    flag = True
    names = request.args.to_dict()
    for name, values in names.items():
        if flag:
            for value in values:
                if value == "BenchmarkTest02344":
                    param = name
                    s23423 = param
                    a12341 = StringHolder()
                    def lmd(s: StringHolder) -> None:
                        def innerLmd(p: StringHolder) -> None:
                            p.value = "";
                        innerLambda = UnaryOpMutation(innerLmd)
                        innerLambda.mutate(s)
                        s.value = s23423
                    lambda1231 = UnaryOpMutation(lmd)
                    lambda1231.mutate(a12341)
                    param = a12341.value
                    flag = False
                    break

    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_html(str(e))
        return response

    return response

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def get_insecure_os_command_string():
    # Assuming this method is defined in your helper
    return "your_insecure_os_command"

def escape_html(text):
    # Replace special HTML characters to avoid XSS
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
