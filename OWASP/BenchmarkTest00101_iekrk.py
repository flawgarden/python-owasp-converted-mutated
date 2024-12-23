from typing import TypeVar
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

from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00101", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("sqli-00/BenchmarkTest00101.html"))
        user_cookie = 'BenchmarkTest00101=bar; Max-Age=180; Secure; Path=' + request.path + '; Domain=' + request.host.split(':')[0]
        resp.set_cookie('BenchmarkTest00101', 'bar', max_age=180, secure=True, path=request.path)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00101' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00101'])
        param = varargsWithGenerics(param, "vcgzi")

        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            statement = cursor.execute(sql, ("foo",))
            results = statement.fetchall()
            # Replace with function to print results
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
