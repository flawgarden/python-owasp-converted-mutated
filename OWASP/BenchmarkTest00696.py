
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00696", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(mimetype='text/html')

    values = request.form.getlist('BenchmarkTest00696')
    param = values[0] if values else ""

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    file_target = os.path.join("testfiles", bar)
    response.set_data(f"Access to file: '{file_target}' created.<br>")
    if os.path.exists(file_target):
        response.set_data(response.get_data(as_text=True) + " And file already exists.<br>")
    else:
        response.set_data(response.get_data(as_text=True) + " But file doesn't exist yet.<br>")
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
