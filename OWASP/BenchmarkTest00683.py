
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00683", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00683", "")
    bar = ""
    
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    try:
        tree = ET.parse('static/employees.xml')
        xmlDocument = tree.getroot()
        
        expression = f"./Employee[@emplid='{bar}']"
        nodeList = xmlDocument.findall(expression)

        output = "Your query results are: <br/>"
        for value in nodeList:
            output += value.text + "<br/>"
        return output
    except (ParseError, FileNotFoundError) as e:
        return f"Error parsing XPath input: '{bar}'", 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
