
from flask import Flask, request, render_template
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00132", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00132", "")
    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    file_name = None
    try:
        file_name = os.path.join("testfiles", bar)  # Assuming TESTFILES_DIR is "testfiles"
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_content = f"The beginning of file: '{file_name}' is:\n\n{b.decode(errors='ignore')}"
            return response_content
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
        return f"Problem getting FileInputStream: {str(e)}"
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
