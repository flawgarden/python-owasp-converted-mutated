
import os
from flask import Flask, request, render_template, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route("/trustbound-00/BenchmarkTest00758", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        values = request.form.getlist("BenchmarkTest00758")
        param = values[0] if values else ""

        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        session['userid'] = bar

        return f"Item: 'userid' with value: '{bar}' saved in session."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
