
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:
    hideSQLErrors = True
    
    @staticmethod
    def execute(sql):
        # Mocked database execution for demonstration purposes
        print(f"Executed SQL: {sql}")

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, param_name):
        return self.request.args.get(param_name)

class ThingInterface:
    def doSomething(self, param):
        return param + " processed"

class ThingFactory:
    @staticmethod
    def createThing():
        return ThingInterface()

@app.route("/sqli-05/BenchmarkTest02451", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    try:
        request_obj = SeparateClassRequest(request)
        param = request_obj.getTheParameter("BenchmarkTest02451")
        if param is None:
            param = ""

        bar = do_something(param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        DatabaseHelper.execute(sql)

        return f"No results can be displayed for query: {sql} <br> because the Spring execute method doesn't return results."
    except Exception as e:
        if DatabaseHelper.hideSQLErrors:
            return "Error processing request."
        else:
            raise BadRequest(str(e))

def do_something(param):
    thing = ThingFactory.createThing()
    bar = thing.doSomething(param)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
