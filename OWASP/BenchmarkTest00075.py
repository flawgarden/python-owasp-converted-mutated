
from flask import Flask, request, render_template
import os
import hashlib
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/hash-00/BenchmarkTest00075", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = app.response_class()
        user_cookie = "BenchmarkTest00075=someSecret; Path={}; Max-Age={}; Secure".format(request.path, 60 * 3)
        response.set_cookie("BenchmarkTest00075", "someSecret", max_age=60*3, secure=True, path=request.path, domain=request.host)
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        
        if "BenchmarkTest00075" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest00075"])

        bar = param if (7 * 42) - 106 <= 200 else "This should never happen"
        
        try:
            algorithm = "SHA5"  # Replace with actual logic to read from a properties file if needed
            md = hashlib.new(algorithm)
            input_data = b'?'
            input_param = bar.encode() if isinstance(bar, str) else bar
            
            md.update(input_param)
            result = md.digest()

            file_target = os.path.join("path/to/testfiles/", "passwordFile.txt")
            with open(file_target, "a") as fw:
                fw.write("hash_value=" + result.hex() + "\n")  # Using hex format for simplicity
            
            return f"Sensitive value '{input_param.decode()}' hashed and stored<br/>" + \
                   "Hash Test hashlib.new({}) executed".format(algorithm)
        except Exception as e:
            print("Problem executing hash - TestCase", e)
            return "Error: {}".format(str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
