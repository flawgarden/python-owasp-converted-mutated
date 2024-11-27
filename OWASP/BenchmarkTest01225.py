
import os
import urllib.parse
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01225", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if 'BenchmarkTest01225' in request.headers:
        param = request.headers['BenchmarkTest01225']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('static/employees.xml')
        xml_document = tree.getroot()

        expression = f"./Employees/Employee[@emplid='{bar}']"
        result = xml_document.findall(expression)

        response_result = "Your query results are: " + str(result) + "<br/>"
        return response_result

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'", 500

class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
