
import os
from flask import Flask, request, render_template, make_response
from xml.etree import ElementTree as ET
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01894", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest01894.html"))
        user_cookie = ('BenchmarkTest01894', '2222', 180)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01894' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01894'])

        bar = do_something(request, param)

        try:
            with open('employees.xml', 'rb') as file:
                xml_document = ET.parse(file)
                expression = f".//Employee[@emplid='{bar}']"
                result = xml_document.find(expression)

                if result is not None:
                    response_text = f"Your query results are: {ET.tostring(result).decode()}<br/>"
                else:
                    response_text = "No results found<br/>"

                return response_text

        except ET.ParseError as e:
            return f"Error parsing XML input: '{bar}'", 500

def do_something(request, param):
    num = 106
    return param if (7 * 42) - num <= 200 else "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
