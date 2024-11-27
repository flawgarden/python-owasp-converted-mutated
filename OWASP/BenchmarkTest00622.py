
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00622", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = request.form.get('BenchmarkTest00622', '')
    bar = ''
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

    file_target = os.path.join('path/to/testfiles_dir', bar)
    response_data = f"Access to file: '{file_target}' created.<br>"
    
    if os.path.exists(file_target):
        response_data += " And file already exists."
    else:
        response_data += " But file doesn't exist yet."
    
    response.set_data(response_data)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
