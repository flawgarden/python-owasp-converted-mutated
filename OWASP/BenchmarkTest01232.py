
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01232", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    param = request.args.get('BenchmarkTest01232', "")
    bar = Test().do_something(request, param)

    file_target = os.path.join("path/to/test/files", bar)
    response_text = f"Access to file: '{file_target}' created.<br>"
    
    if os.path.exists(file_target):
        response_text += " And file already exists."
    else:
        response_text += " But file doesn't exist yet."

    return response_text

class Test:

    def do_something(self, request, param):
        thing = ThingFactory.create_thing()
        bar = thing.do_something(param)
        return bar

class ThingFactory:

    @staticmethod
    def create_thing():
        return Thing()

class Thing:

    def do_something(self, param):
        # Implementation for the method
        return param  # Placeholder implementation

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
