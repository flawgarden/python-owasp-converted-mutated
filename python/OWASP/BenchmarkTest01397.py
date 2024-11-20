
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01397", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01397', '')

        bar = Test().do_something(param)

        try:
            file_path = os.path.join('path_to_your_classpath', 'employees.xml')
            tree = ET.parse(file_path)
            root = tree.getroot()

            expression = f"./Employee[@emplid='{bar}']"
            result = root.find(expression)

            response = f"Your query results are: {ET.tostring(result).decode() if result is not None else 'No results found'}<br/>"
            return response

        except ET.ParseError as e:
            return f"Error parsing XPath input: '{bar}'", 500

    return render_template("index.html")

class Test:

    def do_something(self, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
