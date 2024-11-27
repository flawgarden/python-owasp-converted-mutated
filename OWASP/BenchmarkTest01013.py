
import os
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01013", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = app.response_class(content_type='text/html;charset=UTF-8')
        user_cookie = ('BenchmarkTest01013', '2222', 60 * 3)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True)
        return render_template("xpathi-00/BenchmarkTest01013.html")

    else:
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if 'BenchmarkTest01013' in cookies:
            param = unquote(cookies['BenchmarkTest01013'])

        bar = Test().do_something(request, param)

        try:
            tree = ET.parse('static/employees.xml')
            root = tree.getroot()
            expression = ".//Employee[@emplid='{}']".format(bar)
            node_list = root.findall(expression)

            output = "Your query results are: <br/>"
            for value in node_list:
                output += value.text + "<br/>"
            return output
        except ET.ParseError as e:
            return "Error parsing XPath input: '{}'".format(html_escape(bar)), 500

class Test:

    def do_something(self, request, param):
        bar = "noCookieValueSupplied"
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

def html_escape(text):
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
