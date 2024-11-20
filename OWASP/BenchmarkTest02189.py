
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest02189", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02189', "")
        bar = do_something(request, param)

        try:
            tree = ET.parse('static/employees.xml')
            root = tree.getroot()
            expression = f"./Employee[@emplid='{bar}']"

            node_list = root.findall(expression)

            response_content = "Your query results are: <br/>"
            for value in node_list:
                response_content += f"{value.text}<br/>"
            return response_content
        except (ET.ParseError, Exception) as e:
            return f"Error parsing XPath input: '{escape_html(bar)}'", 500

    return render_template("index.html")

def do_something(request, param):
    bar = param
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
