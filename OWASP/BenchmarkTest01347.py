
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01347", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(mimetype='text/html')
    param = request.args.get('BenchmarkTest01347', '')

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    return response

class Test:

    def do_something(self, request, param):
        a81561 = param  # assign
        b81561 = str(a81561) + " SafeStuff"  # stick in string
        b81561 = b81561[:-len("Chars")] + "Chars"  # replace some of the end content
        map81561 = {}
        map81561["key81561"] = b81561  # put in a collection
        c81561 = map81561["key81561"]  # get it back out
        d81561 = c81561[:-1]  # extract most of it
        e81561 = base64.b64decode(base64.b64encode(d81561.encode())).decode()  # B64 encode and decode it
        f81561 = e81561.split(" ")[0]  # split it on a space
        thing = ThingFactory.create_thing()
        bar = thing.do_something(f81561)  # reflection

        return bar

class ThingFactory:
    @staticmethod
    def create_thing():
        return Thing()

class Thing:
    def do_something(self, f81561):
        return f81561

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
