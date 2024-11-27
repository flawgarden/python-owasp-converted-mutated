
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest00852", methods=['GET', 'POST'])
def benchmark_test_00852():
    if request.method == 'POST' or request.method == 'GET':
        query_string = request.query_string.decode('utf-8')
        paramval = "BenchmarkTest00852="
        param_loc = query_string.find(paramval)

        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest00852' in query string."

        param = query_string[param_loc + len(paramval):]
        ampersand_loc = query_string.find("&", param_loc)

        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]

        param = urllib.parse.unquote(param)

        bar = "safe!"
        map47458 = {
            "keyA-47458": "a_Value",
            "keyB-47458": param,
            "keyC": "another_Value"
        }
        bar = map47458["keyB-47458"]
        bar = map47458["keyA-47458"]

        try:
            tree = ET.parse('static/employees.xml')
            xml_document = tree.getroot()

            expression = f".//Employee[@emplid='{bar}']"
            result = xml_document.find(expression)

            if result is not None:
                response_result = ET.tostring(result, encoding='unicode')
            else:
                response_result = "No results found."

            return f"Your query results are: {response_result}<br/>"

        except Exception as e:
            return f"Error parsing XPath input: '{bar}'"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
