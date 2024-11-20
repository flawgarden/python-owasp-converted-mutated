
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest02457", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = ""
    param = request.form.get("BenchmarkTest02457", "")

    bar = do_something(request, param)

    try:
        tree = ET.parse('static/employees.xml')
        xml_document = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        result = xml_document.findall(expression)

        response_content += "Your query results are: " + str(result) + "<br/>"

    except ParseError as e:
        response_content += "Error parsing XPath input: '" + bar + "'"
        raise e

    return response_content

def do_something(request, param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the first safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
