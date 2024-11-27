
import os
from flask import Flask, request, render_template, make_response
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest01893", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest01893.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01893", "2222", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest01893", "2222", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    param = "noCookieValueSupplied"
    if request.cookies.get("BenchmarkTest01893"):
        param = request.cookies.get("BenchmarkTest01893")

    bar = do_something(param)

    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()
        expression = f".//Employee[@emplid='{bar}']"
        node_list = root.findall(expression)

        results = "Your query results are: <br/>"
        for value in node_list:
            results += value.text + "<br/>"
        return results
    except ET.ParseError as e:
        return f"Error parsing XPath input: '{bar}'", 500


def do_something(param):
    bar = param
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
