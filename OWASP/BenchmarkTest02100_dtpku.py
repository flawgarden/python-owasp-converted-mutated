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
import urllib.parse
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest02100", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if 'BenchmarkTest02100' in request.headers:
        param = request.headers['BenchmarkTest02100']  # just grab first element
    my_tuple = (param, "bytpg", "dwkkc")
    a, b, c = my_tuple
    param = a

    param = urllib.parse.unquote(param)  # URL Decode the header value

    bar = do_something(param)

    try:
        tree = ET.parse('static/employees.xml')  # Assuming the XML file is placed in static folder
        root = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        node_list = root.findall(expression)

        response_output = "Your query results are: <br/>"
        for value in node_list:
            response_output += f"{value.text}<br/>"
        return response_output

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'<br/>{str(e)}"

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
