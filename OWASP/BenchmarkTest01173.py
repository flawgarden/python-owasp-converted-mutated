
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01173", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return handle_post_request()

def handle_post_request():
    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    referer_header = request.headers.get("Referer")

    if referer_header:
        param = referer_header

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = []
            values_list.append("safe")
            values_list.append(param)
            values_list.append("moresafe")

            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[0]  # get the param value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
