
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01633", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    values = request.form.getlist("BenchmarkTest01633")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('employees.xml')
        xml_document = tree.getroot()
        expression = f"./Employee[@emplid='{bar}']"
        result = xml_document.find(expression)

        if result is not None:
            response_text = f"Your query results are: {ET.tostring(result).decode()}<br/>"
        else:
            response_text = "No results found"

        return response_text

    except ET.ParseError as e:
        return f"Error parsing XPath input: '{bar}'", 500

class Test:

    def do_something(self, request, param):
        a31144 = param
        b31144 = a31144 + " SafeStuff"
        b31144 = b31144[:-1] + "Chars"
        c31144 = b31144

        d31144 = c31144[:-1]
        e31144 = b64decode(b64encode(d31144.encode())).decode()
        f31144 = e31144.split(" ")[0]

        thing = ThingFactory.create_thing()
        g31144 = "barbarians_at_the_gate"
        bar = thing.do_something(g31144)

        return bar

class ThingFactory:

    @staticmethod
    def create_thing():
        return Thing()

class Thing:

    def do_something(self, data):
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
