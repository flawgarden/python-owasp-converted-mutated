
from flask import Flask, request, make_response, render_template
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02144", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest02144", "")

    bar = do_something(param)

    if bar == "":
        bar = "No cookie value supplied"

    response.set_cookie("SomeCookie", bar, secure=True, httponly=True, path=request.path)

    response_data = f"Created cookie: 'SomeCookie': with value: '{html.escape(bar)}' and secure flag set to: true"
    response.data = response_data
    return response

def do_something(param):
    return html.escape(param)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
