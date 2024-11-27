
from flask import Flask, request, session, escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key_here'

@app.route("/trustbound-00/BenchmarkTest00756", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist('BenchmarkTest00756')
        param = values[0] if values else ""

        bar = escape(param)

        session['userid'] = bar

        return "Item: 'userid' with value: '{}' saved in session.".format(bar)

    return "Invalid request method."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
