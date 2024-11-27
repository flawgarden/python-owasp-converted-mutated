
import os
from flask import Flask, request, render_template, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00117", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest00117.html"))
        user_cookie = ('BenchmarkTest00117', '2222', '/', None, True, 60*3)
        response.set_cookie(*user_cookie)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest00117' in the_cookies:
            param = the_cookies['BenchmarkTest00117']

        bar = param
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"

        try:
            tree = ET.parse('employees.xml')
            root = tree.getroot()
            expression = "./Employee[@emplid='{}']".format(bar)
            results = root.findall(expression)

            response_text = "Your query results are: <br/>"
            for value in results:
                response_text += value.text + "<br/>"

            return response_text
        except ET.ParseError as e:
            return "Error parsing XPath input: '{}'".format(escape_html(bar)), 500

def escape_html(text):
    return (text.replace("&", "&amp;")
                  .replace("<", "&lt;")
                  .replace(">", "&gt;")
                  .replace('"', "&quot;")
                  .replace("'", "&#039;"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
