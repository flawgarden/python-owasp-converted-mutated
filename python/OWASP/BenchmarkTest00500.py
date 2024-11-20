
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00500", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()  # Redirect GET requests to POST logic

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ''
    map = request.args
    if map:
        values = map.getlist("BenchmarkTest00500")
        if values:
            param = values[0]

    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Adjust command as needed for your environment

    args_env = {"Foo": "bar"}
    
    try:
        p = os.popen(cmd + bar)  # Execute the command
        output = p.read()  # Get the output from the command
        response.data = output.encode('utf-8')  # Update response with command output
    except Exception as e:
        print("Problem executing cmd - TestCase")
        response.data = str(e).encode('utf-8')
        return response

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
