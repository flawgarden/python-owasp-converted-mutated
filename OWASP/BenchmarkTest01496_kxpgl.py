from typing import Any
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

@app.route("/pathtraver-01/BenchmarkTest01496", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.form.get('BenchmarkTest01496', '')

        bar = Test().do_something(request, param)

        file_name = None
        try:
            file_name = os.path.join('path_to_test_files', bar)
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                response_data = f"The beginning of file: '{file_name}' is:\n\n"
                response_data += b.decode('utf-8', errors='ignore')
                return response_data
        except Exception as e:
            print(f"Couldn't open file: '{file_name}'")
        return "Error occurred."

class Test:

    def do_something(self, request, param):
        bar = None
        guess = "ABC"
        param = simplePatternMatchingString1(param)
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



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
