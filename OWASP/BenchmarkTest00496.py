
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00496", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = "<html><body>"
    param = request.args.get('BenchmarkTest00496', '')

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        results = process.read()
        response += results
        process.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += str(e)
    
    response += "</body></html>"
    return response

def get_insecure_os_command_string():
    return "echo"  # Example command; adjust as necessary

if __name__ == "__main__":
    app.run(host='0.0.0.0')
