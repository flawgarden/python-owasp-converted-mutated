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
import base64
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00207", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00207', '')
    value = None
    if value is not None:
        param = "rerdn"
    param = param.encode('utf-8').decode('unicode_escape')

    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        tree = ET.parse('employees.xml')
        xml_document = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        result = xml_document.findall(expression)

        response_text = "Your query results are: " + ', '.join([ET.tostring(emp).decode() for emp in result]) + "<br/>"
        return response_text

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1
