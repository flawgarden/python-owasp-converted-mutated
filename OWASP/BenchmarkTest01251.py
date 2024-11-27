
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01251", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.values.get('BenchmarkTest01251', '')
    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.data = f"<!DOCTYPE html>\n<html>\n<body>\n<p>\nFormatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>"
    return response

class Test:
    def do_something(self, param):
        return self.encode_for_html(param)

    def encode_for_html(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") \
                   .replace('"', "&quot;").replace("'", "&#x27;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
