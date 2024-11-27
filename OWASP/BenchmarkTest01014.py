
import os
from flask import Flask, request, render_template, make_response
import xml.etree.ElementTree as ET
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xpathi-00/BenchmarkTest01014", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("xpathi-00/BenchmarkTest01014.html"))
        user_cookie = ('BenchmarkTest01014', '2222', {'max_age': 60*3, 'secure': True, 'path': request.path, 'domain': request.host})
        response.set_cookie(*user_cookie)
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01014' in cookies:
            param = unquote(cookies['BenchmarkTest01014'])

        bar = Test().do_something(param)

        try:
            tree = ET.parse('employees.xml')
            root = tree.getroot()

            expression = f".//Employee[@emplid='{bar}']"
            result = root.find(expression)

            response_text = "Your query results are: " + (ET.tostring(result).decode() if result is not None else "No results found") + "<br/>"
            return response_text

        except ET.ParseError as e:
            return "Error parsing XML input: '" + bar + "'"

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bob"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bob's your uncle"

        return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
