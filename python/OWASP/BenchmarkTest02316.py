
from flask import Flask, request, Response
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-04/BenchmarkTest02316", methods=['GET', 'POST'])
def benchmark_test_02316():
    if request.method == 'GET':
        return benchmark_test_02316_post()
    return benchmark_test_02316_post()


def benchmark_test_02316_post():
    param = ""
    flag = True
    names = request.args.to_dict().keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02316":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    response = Response()
    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(bar % tuple(obj))
    response.content_type = "text/html;charset=UTF-8"
    
    return response


def do_something(param):
    thing = ThingFactory.create_thing()
    bar = thing.do_something(param)

    return bar


class ThingInterface:
    def do_something(self, param):
        return "Processed: " + str(param)


class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
