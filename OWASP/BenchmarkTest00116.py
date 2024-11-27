
import os
from flask import Flask, request, render_template, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest00116", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest00116.html"))
        user_cookie = ("BenchmarkTest00116", "2222")
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=60 * 3, secure=True)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00116' in cookies:
            param = cookies['BenchmarkTest00116']

        bar = "safe!"
        map51005 = {
            "keyA-51005": "a_Value",
            "keyB-51005": param,
            "keyC": "another_Value"
        }
        bar = map51005["keyB-51005"]
        bar = map51005["keyA-51005"]

        try:
            tree = ET.parse(os.path.join('path_to_resources', 'employees.xml'))
            xml_document = tree.getroot()

            expression = f".//Employee[@emplid='{bar}']"
            node_list = xml_document.findall(expression)

            response_text = "Your query results are: <br/>"
            for value in node_list:
                response_text += f"{value.text}<br/>"

            return response_text
        except ET.ParseError as e:
            return f"Error parsing XPath input: '{bar}'", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
