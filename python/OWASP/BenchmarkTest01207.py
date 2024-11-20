
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = "safe!"
        map95902 = {}
        map95902["keyA-95902"] = "a_Value"  # put some stuff in the collection
        map95902["keyB-95902"] = param  # put it in a collection
        map95902["keyC"] = "another_Value"  # put some stuff in the collection
        bar = map95902.get("keyB-95902")  # get it back out
        bar = map95902.get("keyA-95902")  # get safe value back out

        return bar

@app.route("/trustbound-00/BenchmarkTest01207", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        param = ""
        headers = request.headers.getlist("BenchmarkTest01207")

        if headers:
            param = headers[0]  # just grab the first element

        param = urllib.parse.unquote(param)  # URL Decode the header value

        bar = Test().do_something(param)

        # Set session attribute
        request.environ['beaker.session'][bar] = "10340"

        return f"Item: '{bar}' with value: '10340' saved in session."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
