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

@app.route("/pathtraver-02/BenchmarkTest02466", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "<html><body>"

    values = request.values.getlist("BenchmarkTest02466")
    param = values[0] if values else ""

    bar = do_something(param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join('testfiles', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_content += (
                "The beginning of file: '"
                + escape_html(file_name)
                + "' is:<br/><br/>"
                + escape_html(b.decode('utf-8', errors='ignore'))
            )
    except Exception as e:
        response_content += (
            "Problem getting FileInputStream: "
            + escape_html(str(e))
        )

    response_content += "</body></html>"
    return response_content

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    tmpUnique42 = bar
    for i in range(0, 1000, 16767):
        bar = tmpUnique42
    else:
        bar = "bobs_your_uncle"

    return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
