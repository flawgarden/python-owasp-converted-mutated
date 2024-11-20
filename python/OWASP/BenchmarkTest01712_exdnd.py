#Snyk original results: [89]
#Bearer original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: [89]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest01712.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/decorator/decorator.tmt with name simple_class_decorator_positive 
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

from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01712", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode('utf-8')
    query_string = example_function_with_class_wr(query_string, "postfix")
    paramval = "BenchmarkTest01712="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01712' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = f"{{call {bar}}}"
    
    try:
        connection = sqlite3.connect('database.db')  # Replace with actual db connection
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return str(results)

    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, request, param):
        bar = "safe!"
        map_6261 = {
            "keyA-6261": "a-Value", 
            "keyB-6261": param, 
            "keyC": "another-Value"
        }
        bar = map_6261["keyB-6261"]
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')



def wrapperExample(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper



def wrapperExample2(func):
    def wrapper(*args, **kwargs):
        args = ("fixed_string",) + args[1:]
        result = func(*args, **kwargs)
        return result
    return wrapper



def wrapperExampleMemoization(func):
    cache = ["result"]
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache.append(result)
        return cache[-1]
    return wrapper



def wrapperExampleMemoizationNegative(func):
    cache = ["result"]
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache.append(result)
        return cache[0]
    return wrapper



@wrapperExample
def example_function(x, y):
    return x + y



@wrapperExampleMemoization
def example_function_memo_positive(x, y):
    return x + y



@wrapperExampleMemoizationNegative
def example_function_memo_negative(x, y):
    return x + y



@wrapperExample2
def example_function_2(x, y):
    return x + y



@ClassWrapper
def example_function_with_class_wr(x, y):
    return x + y



@ClassWrapperEmpty
def example_function_with_empty_class_wr(x, y):
    return x + y
