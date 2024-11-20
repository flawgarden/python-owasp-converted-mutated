
import os
from flask import Flask, request, render_template, escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00888", methods=['GET', 'POST'])
def benchmark_test_00888():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00888', '')
        bar = escape(param)

        response = app.response_class(
            response=bar,
            status=200,
            mimetype='text/html'
        )
        response.headers['X-XSS-Protection'] = '0'
        return response
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
