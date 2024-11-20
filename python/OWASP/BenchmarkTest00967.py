
import os
import urllib.parse
from flask import Flask, request, render_template, make_response
import hashlib

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-01/BenchmarkTest00967", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("hash-01/BenchmarkTest00967.html"))
        user_cookie = 'BenchmarkTest00967=someSecret; Max-Age=180; Path={}; Secure; Domain={}'.format(
            request.path, request.host)
        response.set_cookie("BenchmarkTest00967", value="someSecret", max_age=180, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00967" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest00967"])

        bar = Test().do_something(request, param)

        try:
            algorithm = "SHA5"  # Placeholder for reading from benchmark.properties
            md = hashlib.new(algorithm)
            input_data = bytes(bar, 'utf-8')
            md.update(input_data)

            result = md.digest()
            file_target = os.path.join("testfiles", "passwordFile.txt")
            with open(file_target, 'a') as fw:
                fw.write("hash_value={}\n".format(result.hex()))  # Storing hex representation

            return ("Sensitive value '{}' hashed and stored<br/>".format(urllib.parse.quote(input_data.decode('utf-8'))))

        except Exception as e:
            print("Problem executing hash - TestCase")
            return str(e), 500

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param != "noCookieValueSupplied":
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
