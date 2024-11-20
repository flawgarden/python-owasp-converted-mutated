
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest01478", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "Your query results are: <br/>"
    param = ""
    flag = True

    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01478":
                    param = name
                    flag = False
                    break

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        expression = ".//Employee[@emplid='{}']".format(bar)
        node_list = root.findall(expression)

        for value in node_list:
            response_content += value.text + "<br/>"

    except ET.ParseError as e:
        response_content += "Error parsing XPath input: '{}'".format(bar)
        raise Exception(e)

    return response_content


class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
