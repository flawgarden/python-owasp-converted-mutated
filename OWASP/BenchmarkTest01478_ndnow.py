#Snyk original results: [643]
#CodeQL original results: [643]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [611, 643, 79]
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest01478.py
#Original file CWE's: [643]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/duck/typing.tmt with name duck_typing_hasattr_check_negative 
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
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest01478", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "Your query results are: <br/>"
    param = ""
    flag = True

    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01478":
                    param = name
                    duck_like = DefinitelyNotADuck()
                    param = make_it_quack_attr(duck_like, param)
                    flag = False
                    break

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        expression = ".//Employee[@emplid='{}']".format(bar)
        node_list = root.findall(expression)

        for value in node_list:
            response_content += value.text + "<br/>"

    except ET.ParseError as e:
        response_content += "Error parsing XPath input: '{}'".format(bar)
        raise Exception(e)

    return response_content


class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
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
