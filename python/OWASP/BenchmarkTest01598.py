
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01598", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest01598")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    response = app.response_class(response=bar, status=200, mimetype=response_content)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:

    def do_something(self, param):
        a75770 = param
        b75770 = str(a75770) + " SafeStuff"
        b75770 = b75770[:-len("Chars")] + "Chars"
        
        map75770 = {"key75770": b75770}
        c75770 = map75770["key75770"]
        d75770 = c75770[:-1]
        
        e75770 = d75770.encode('utf-8').decode('utf-8')  # Simulating Base64 encode/decode
        f75770 = e75770.split(" ")[0]

        thing = ThingFactory.create_thing()
        bar = thing.do_something(f75770)

        return bar

class ThingFactory:
    
    @staticmethod
    def create_thing():
        return ThingInterface()

class ThingInterface:

    def do_something(self, input):
        return f"Processed: {input}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
