
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00442", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = request.form.get("BenchmarkTest00442", "")

    bar = param if (7 * 42) - 106 <= 200 else "This should never happen"

    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        expression = "./Employee[@emplid='{}']".format(bar)
        result = root.findall(expression)

        response += "Your query results are: " + str([ET.tostring(emp) for emp in result]) + "<br/>"

    except ET.ParseError as e:
        response += "Error parsing XPath input: '" + escape(bar) + "'"
        raise Exception(e)

    return render_template("response.html", response=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
