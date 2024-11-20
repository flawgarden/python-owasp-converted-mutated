
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/pathtraver-00/BenchmarkTest00062", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00062.html"))
        user_cookie = ('BenchmarkTest00062', 'FileName', None, None, '/', None, 'Secure')
        response.set_cookie(*user_cookie, max_age=60 * 3)
        return response
    else:
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00062' in cookies:
            param = unquote(cookies['BenchmarkTest00062'])

        bar = "safe!"
        map77232 = {
            "keyA-77232": "a-Value",
            "keyB-77232": param,
            "keyC": "another-Value"
        }
        bar = map77232["keyB-77232"]

        file_name = None
        try:
            file_name = os.path.join("path/to/testfiles/dir", bar)  # Replace with actual path
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
        except Exception as e:
            return f"Problem getting FileInputStream: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
