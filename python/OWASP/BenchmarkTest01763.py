
import os
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/hash-02/BenchmarkTest01763", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Flask.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.values.get("BenchmarkTest01763", '')

    bar = Test().do_something(param)

    try:
        md = hashlib.sha256()
        input_data = b'?'
        if isinstance(bar, str):
            input_data = bar.encode()
        
        md.update(input_data)

        result = md.digest()
        file_target = os.path.join(os.path.dirname(__file__), "passwordFile.txt")
        with open(file_target, 'a') as fw:
            fw.write("hash_value=" + result.hex() + "\n")
        
        response.set_data(f"Sensitive value '{input_data.decode()}' hashed and stored<br/>")

    except Exception as e:
        print("Problem executing hash - TestCase", e)
        raise 

    response.set_data(response.get_data(as_text=True) + "Hash Test executed")
    return response

class Test:

    def do_something(self, param):
        thing = ThingFactory.create_thing()
        bar = thing.do_something(param)
        return bar

class ThingInterface:
    def do_something(self, param):
        return param

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
