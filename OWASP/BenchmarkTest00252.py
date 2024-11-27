
import os
from flask import Flask, request, render_template, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route("/trustbound-00/BenchmarkTest00252", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = ""
        for name in request.headers:
            if name not in ['User-Agent', 'Accept', 'Accept-Encoding', 'Accept-Language', 'Connection']:  # Common headers
                param = name
                break

        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        session[bar] = "10340"

        return f"Item: '{bar}' with value: '10340' saved in session."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
