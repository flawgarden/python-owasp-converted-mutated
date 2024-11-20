
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class Test:
    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar


@app.route("/xpathi-00/BenchmarkTest01562", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response_content = ""

    param = request.args.get('BenchmarkTest01562', "")
    bar = Test().do_something(param)

    try:
        tree = ET.parse('employees.xml')
        xml_document = tree.getroot()

        expression = f"./Employees/Employee[@emplid='{bar}']"
        node_list = xml_document.findall(expression)

        response_content += "Your query results are: <br/>"

        for value in node_list:
            response_content += f"{value.text}<br/>"
    except Exception as e:
        response_content += f"Error parsing XPath input: '{bar}'"
        raise Exception(e)

    return response_content


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
