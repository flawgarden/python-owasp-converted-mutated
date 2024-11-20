
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00366", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00366", "")
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

    file_name = os.path.join('testfiles', bar)
    is_file = None

    try:
        with open(file_name, 'rb') as is_file:
            b = is_file.read(1000)
            response_body = f"The beginning of file: '{file_name}' is:\n\n"
            response_body += str(b, 'utf-8', 'ignore')
            return response_body
    except Exception as e:
        print(f"Couldn't open InputStream on file: '{file_name}'")
        return f"Problem getting InputStream: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
