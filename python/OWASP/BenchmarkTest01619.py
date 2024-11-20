
from flask import Flask, request, session, render_template
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'

@app.route("/trustbound-01/BenchmarkTest01619", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist("BenchmarkTest01619")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        session['userid'] = bar

        return f"Item: 'userid' with value: '{html.escape(bar)}' saved in session."
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = html.escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
