
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00923", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest00923", "")

        bar = param  # Assuming we are not applying any escaping for simplicity here

        # Store in session
        request.environ['session']['userid'] = bar

        return f"Item: 'userid' with value: '{bar}' saved in session."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
