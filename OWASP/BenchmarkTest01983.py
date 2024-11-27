
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path/to/testfiles'  # Update with the correct path

@app.route("/pathtraver-02/BenchmarkTest01983", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    for header in request.headers:
        if header in ['User-Agent', 'Accept', 'Accept-Language', 'Content-Type']:  # Common headers, update as needed
            continue  # If standard header, move on to next one
        
        param = header  # Grabs the name of the first non-standard header as the parameter
        break

    bar = do_something(request, param)

    file_target = os.path.join(TESTFILES_DIR, bar)
    response.body = f"Access to file: '{file_target}' created."
    
    if os.path.exists(file_target):
        response.body += " And file already exists."
    else:
        response.body += " But file doesn't exist yet."

    return response

def do_something(request, param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
