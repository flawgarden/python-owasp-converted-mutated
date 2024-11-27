
import os
from flask import Flask, request, render_template
import base64
import sqlalchemy

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01301", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest01301', '')

    bar = Test().do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlalchemy.create_engine('sqlite:///your-database.db').connect()
        result = connection.execute(sql)
        print_results(result, sql)
    except sqlalchemy.exc.SQLAlchemyError as e:
        response.data = b"Error processing request."
        return response

    return response

class Test:

    def do_something(self, param):
        a11416 = param
        b11416 = a11416 + " SafeStuff"
        b11416 = b11416[:-len("Chars")] + "Chars"

        map11416 = {}
        map11416["key11416"] = b11416
        c11416 = map11416["key11416"]
        d11416 = c11416[:-1]
        e11416 = base64.b64decode(base64.b64encode(d11416.encode())).decode()
        f11416 = e11416.split(" ")[0]

        thing = create_thing()
        g11416 = "barbarians_at_the_gate"
        bar = thing.do_something(g11416)

        return bar

def print_results(result, sql):
    for row in result:
        print(row)

def create_thing():
    class Thing:
        def do_something(self, g11416):
            return g11416

    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
