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

import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01734", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest01734="
    param_loc = query_string.find(paramval)
    queue787231 = SimpleQueue()
    queue787231.put("")
    query_string = queue787231.get()

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01734' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('employees.xml')
        xml_document = tree.getroot()

        expression = f"./Employees/Employee[@emplid='{bar}']"
        node_list = xml_document.findall(expression)

        output = "Your query results are: <br/>"

        for value in node_list:
            output += f"{value.text}<br/>"

        return output

    except ET.ParseError as e:
        return f"Error parsing XPath input: '{bar}'"

class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
