
import os
from flask import Flask, request, render_template
import base64
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00207", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00207', '')
    param = param.encode('utf-8').decode('unicode_escape')
    
    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        tree = ET.parse('employees.xml')
        xml_document = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        result = xml_document.findall(expression)

        response_text = "Your query results are: " + ', '.join([ET.tostring(emp).decode() for emp in result]) + "<br/>"
        return response_text

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
