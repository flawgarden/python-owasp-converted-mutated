
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02052", methods=['GET', 'POST'])
def benchmark_test_02052():
    if request.method == 'GET':
        return benchmark_test_02052_post()

    return benchmark_test_02052_post()

def benchmark_test_02052_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = [bar, "b"]
    response.set_data(f"Formatted like: {obj[0]} and {obj[1]}.")
    return response

def do_something(param):
    bar = "safe!"
    map20081 = {
        "keyA-20081": "a_Value",  # put some stuff in the collection
        "keyB-20081": param,      # put it in a collection
        "keyC": "another_Value"    # put some stuff in the collection
    }
    bar = map20081.get("keyB-20081")  # get it back out
    bar = map20081.get("keyA-20081")  # get safe value back out

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
