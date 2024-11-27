
import os
from flask import Flask, request, render_template, make_response
import xml.etree.ElementTree as ET
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest01892", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("xpathi-00/BenchmarkTest01892.html"))
        user_cookie = 'BenchmarkTest01892=2222'
        resp.set_cookie('BenchmarkTest01892', '2222', max_age=60 * 3, secure=True, path=request.path, domain=request.host_url.split("//")[-1].split("/")[0])
        return resp

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01892' in cookies:
            param = unquote(cookies['BenchmarkTest01892'])

        bar = do_something(param)

        try:
            tree = ET.parse('static/employees.xml')
            root = tree.getroot()
            expression = f"./Employee[@emplid='{bar}']"
            result = root.findall(expression)

            output = "Your query results are: <br/>"
            for value in result:
                output += value.text + "<br/>"
            return output
        except ET.ParseError as e:
            return f"Error parsing XPath input: '{bar}'", 500

def do_something(param):
    map3451 = {}
    map3451['keyA-3451'] = 'a-Value'
    map3451['keyB-3451'] = param
    map3451['keyC'] = 'another-Value'
    bar = map3451['keyB-3451']
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
