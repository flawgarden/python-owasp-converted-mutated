
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/trustbound-00/BenchmarkTest00424", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class(
            content_type='text/html;charset=UTF-8'
        )

        param = request.form.get("BenchmarkTest00424", "")
        bar = ""

        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()

        request.environ['werkzeug.wrappers']._SessionInterface['userid'] = bar

        response.set_data(
            "Item: 'userid' with value: '"
            + bar.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            + "' saved in session."
        )

        return response
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
