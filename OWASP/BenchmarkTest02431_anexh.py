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

@app.route("/cmdi-02/BenchmarkTest02431", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = os.popen('echo "Processing request..."').read()

        param = request.form.get('BenchmarkTest02431', '')
        bar = do_something(param)
        my_tuple = (bar, "grept", "hhiui")
        my_list = list(my_tuple)
        my_list[0] = "ynaky"
        new_tuple = tuple(my_list)
        bar = new_tuple[0]

        cmd = "some_command"  # Replace with the actual command you want to run
        args = [cmd]
        args_env = [bar]

        try:
            result = os.popen(f"{cmd} {bar}").read()
            response += result
        except Exception as e:
            response += f"Problem executing cmdi - TestCase: {e}"

        return response

    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-58889": "a-Value",
        "keyB-58889": param,
        "keyC": "another-Value"
    }
    bar = map_["keyB-58889"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
