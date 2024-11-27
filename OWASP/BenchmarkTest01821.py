
import os
from flask import Flask, request, render_template
from xml.etree import ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01821", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01821')
        bar = Test().do_something(request, param)

        try:
            file_path = os.path.join(os.path.dirname(__file__), 'employees.xml')
            tree = ET.parse(file_path)
            xml_document = tree.getroot()

            expression = f".//Employee[@emplid='{bar}']"
            result = xml_document.findall(expression)

            response_result = ", ".join([ET.tostring(e).decode() for e in result])
            return f"Your query results are: {response_result}<br/>"

        except Exception as e:
            return f"Error parsing XPath input: '{bar}'", 500

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = None
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
