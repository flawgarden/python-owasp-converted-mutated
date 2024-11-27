
from flask import Flask, request, session, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Required for session management

@app.route("/trustbound-00/BenchmarkTest00425", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest00425", "")
        sbxyz2192 = str(param)
        bar = sbxyz2192 + "_SafeStuff"

        session['userid'] = bar

        return render_template("response.html", message="Item: 'userid' with value: '{}' saved in session.".format(bar))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
