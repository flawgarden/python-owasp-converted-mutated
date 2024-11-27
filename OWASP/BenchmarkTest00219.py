
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = '/path/to/testfiles/'  # Update with your test files directory

@app.route("/pathtraver-00/BenchmarkTest00219", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = ""

    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Content-Type']:  # Example common headers
            continue
        
        param = name
        break

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    file_name = None
    try:
        file_name = os.path.join(TESTFILES_DIR, bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_content = (
                "The beginning of file: '"
                + file_name
                + "' is:\n\n"
                + b.decode('utf-8', 'ignore')
            )
            return response_content
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return f"Problem getting file: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
