
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00754", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.getlist("BenchmarkTest00754")[0] if request.form.getlist("BenchmarkTest00754") else ""
        bar = "safe!"
        map_6425 = {
            "keyA-6425": "a-Value",
            "keyB-6425": param,
            "keyC": "another-Value"
        }
        bar = map_6425["keyB-6425"]

        # Simulated session variable
        request.environ['beaker.session']['userid'] = bar

        return f"Item: 'userid' with value: '{bar}' saved in session."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
