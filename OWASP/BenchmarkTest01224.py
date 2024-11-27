
from flask import Flask, request, render_template
import urllib.parse
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01224", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.getlist('BenchmarkTest01224')

    if headers:
        param = headers[0]  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    try:
        file = 'employees.xml'
        tree = ET.parse(file)
        root = tree.getroot()

        expression = f"./Employees/Employee[@emplid='{bar}']"
        result = root.find(expression)

        if result is not None:
            response_result = ET.tostring(result).decode()
        else:
            response_result = "No results found."

        return f"Your query results are: {response_result}<br/>"

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'"

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
