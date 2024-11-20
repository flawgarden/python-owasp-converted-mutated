
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01735", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest01735="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01735' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = unquote(param)

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('static/employees.xml')
        root = tree.getroot()

        expression = f"./Employees/Employee[@emplid='{bar}']"
        node_list = root.findall(expression)

        results = "Your query results are: <br/>"
        for value in node_list:
            results += f"{ET.tostring(value, encoding='unicode')}<br/>"
        return results

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'"

class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
