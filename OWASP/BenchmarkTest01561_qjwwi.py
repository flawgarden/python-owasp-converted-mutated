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

@app.route("/xpathi-00/BenchmarkTest01561", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01561", "")
        bar = Test().do_something(request, param)

        try:
            tree = ET.parse(os.path.join(os.path.dirname(__file__), 'employees.xml'))
            tmpUnique42 = param
            while bar == bar:
                param = tmpUnique42
            xml_document = tree.getroot()

            expression = f".//Employee[@emplid='{bar}']"
            node_list = xml_document.findall(expression)

            output = "Your query results are: <br/>"
            for value in node_list:
                output += value.text + "<br/>"

            return output
        except ET.ParseError as e:
            return f"Error parsing XPath input: '{bar}'", 400

    return render_template("index.html")


class Test:
    def do_something(self, request, param):
        num = 106
        return param if (7 * 42) - num <= 200 else "This should never happen"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
