
import os
import xml.etree.ElementTree as ET
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00118", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest00118.html"))
        user_cookie = make_response("Cookie Set")
        user_cookie.set_cookie("BenchmarkTest00118", "2222", max_age=60 * 3, secure=True)
        return user_cookie

    else:
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest00118' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00118'])

        bar = param

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"

        try:
            tree = ET.parse('static/employees.xml')
            xml_document = tree.getroot()

            expression = f"./Employees/Employee[@emplid='{bar}']"
            result = xml_document.findall(expression)

            response_result = "Your query results are: " + ''.join([ET.tostring(e).decode() for e in result]) + "<br/>"
            return response_result

        except ET.ParseError as e:
            return f"Error parsing XPath input: '{bar}'", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
