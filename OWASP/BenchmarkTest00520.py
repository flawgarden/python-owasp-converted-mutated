
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
import urllib.request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00520", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = request.make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get('BenchmarkTest00520', '')

    bar = ""

    # Simple ? condition that assigns constant to bar on true condition
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    try:
        url = os.path.join(app.static_folder, 'employees.xml')
        tree = ET.parse(url)
        xmlDocument = tree.getroot()

        expression = f"./Employee[@emplid='{bar}']"
        result = xmlDocument.find(expression)

        response.data = f"Your query results are: {ET.tostring(result).decode() if result is not None else 'No results found!'}<br/>"

    except Exception as e:
        response.data = f"Error parsing XPath input: '{bar}'"
        raise e

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
