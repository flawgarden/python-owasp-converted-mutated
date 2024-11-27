
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00218", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Accept-Encoding', 'Connection', 'Host', 'Upgrade-Insecure-Requests']:
            continue
        param = name
        break

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

    start_uri_slashes = "//" if os.name != 'nt' else "/"

    try:
        file_path = os.path.join(start_uri_slashes, 'path_to_testfiles_directory', bar.replace(' ', '_'))
        file_target = os.path.abspath(file_path)
        response_message = f"Access to file: '{file_target}' created."
        
        if os.path.exists(file_target):
            response_message += " And file already exists."
        else:
            response_message += " But file doesn't exist yet."

        return response_message
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
