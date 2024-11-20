
import os
from flask import Flask, request, Response
from xml.etree import ElementTree as ET
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00941", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"
    
    param = request.args.get("BenchmarkTest00941")
    bar = ""

    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        file_path = os.path.join(os.path.dirname(__file__), 'employees.xml')
        tree = ET.parse(file_path)
        root = tree.getroot()

        expression = f"./Employee[@emplid='{bar}']"
        results = root.findall(expression)

        response.data = "Your query results are: <br/>"
        for value in results:
            response.data += value.text + "<br/>"

    except ET.ParseError as e:
        response.data = "Error parsing XPath input: '" + bar + "'"
        response.status_code = 500

    return response

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
