
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00175", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00175', '')

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map50591 = {}
    map50591["keyA-50591"] = "a_Value"
    map50591["keyB-50591"] = param
    map50591["keyC"] = "another_Value"
    bar = map50591["keyB-50591"]
    bar = map50591["keyA-50591"]

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f'{cmd} {" ".join(args_env)}')
        output = p.read()
        return render_template("output.html", output=output)  # Assuming you have an HTML template to display the output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error_message=str(e))  # Assuming you have an error template

def get_insecure_os_command_string():
    return "your_command_here"  # Replace with your actual command string

if __name__ == "__main__":
    app.run(host='0.0.0.0')
