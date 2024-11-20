
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00759", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')
    
    values = request.values.getlist("BenchmarkTest00759")
    param = values[0] if values else ""

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    # Simulating session attribute
    request.environ['werkzeug.session'] = {'userid': bar}

    response.set_data(
        "Item: 'userid' with value: '{}' saved in session.".format(bar)
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
