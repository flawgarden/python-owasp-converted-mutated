
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01479", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01479":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('static/employees.xml')
        xml_document = tree.getroot()

        expression = f"./Employee[@emplid='{bar}']"
        node_list = xml_document.findall(expression)

        response_html = "Your query results are: <br/>"
        for value in node_list:
            response_html += f"{ET.tostring(value, encoding='unicode')}<br/>"

        return response_html
    except ET.ParseError as e:
        return f"Error parsing XPath input: '{bar}'", 500

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
