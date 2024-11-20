
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00816", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00816="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00816' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = "safe!"
    map34260 = {
        "keyA-34260": "a-Value",
        "keyB-34260": param,
        "keyC": "another-Value"
    }
    bar = map34260["keyB-34260"]

    a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
    args = [a1, a2, "echo " + bar]

    try:
        process = os.popen(' '.join(args))
        output = process.read()
        process.close()
        return output
    except Exception as e:
        print("Problem executing cmdi - Error: ", e)
        return "Error executing command"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
