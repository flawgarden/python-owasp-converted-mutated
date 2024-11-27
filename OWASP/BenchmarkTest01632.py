
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, request, param):
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

@app.route("/xpathi-00/BenchmarkTest01632", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = ""
    values = request.values.getlist("BenchmarkTest01632")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('static/employees.xml')
        root = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        node_list = root.findall(expression)

        response_content += "Your query results are: <br/>"

        for value in node_list:
            response_content += value.text + "<br/>"
    except ET.ParseError as e:
        response_content += f"Error parsing XPath input: '{bar}'"
        raise BadRequest(response_content)

    return response_content

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
