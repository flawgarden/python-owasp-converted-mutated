
import os
from flask import Flask, request, render_template
import base64
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00787", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00787="
    paramLoc = query_string.find(paramval)

    if paramLoc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00787' in query string."

    param = query_string[paramLoc + len(paramval):]  # assume "BenchmarkTest00787" param is last
    ampersandLoc = query_string.find("&", paramLoc)

    if ampersandLoc != -1:
        param = query_string[paramLoc + len(paramval):ampersandLoc]

    param = urllib.parse.unquote(param)

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    file_name = None
    fos = None

    try:
        file_name = os.path.join("testfiles", bar)

        fos = open(file_name, 'wb')
        return f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos:
            try:
                fos.close()
            except Exception as e:
                pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
