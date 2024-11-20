
import os
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00599", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        try:
            param = ""
            flag = True
            names = request.args.keys()
            for name in names:
                values = request.values.getlist(name)
                for value in values:
                    if value == "BenchmarkTest00599":
                        param = name
                        flag = False

            a99467 = param
            b99467 = a99467 + " SafeStuff"
            b99467 = b99467[:-5] + "Chars"
            map99467 = {"key99467": b99467}
            c99467 = map99467["key99467"]
            d99467 = c99467[:-1]
            e99467 = d99467.encode('utf-8').decode('utf-8')
            f99467 = e99467.split(" ")[0]
            thing = create_thing()
            g99467 = "barbarians_at_the_gate"
            bar = thing.do_something(g99467)

            sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
            DatabaseHelper.JDBCtemplate.batch_update(sql)
            return f"No results can be displayed for query: {sql} <br> because the method doesn't return results."
        except Exception as e:
            return "Error processing request."

def create_thing():
    return ThingInterface()

class ThingInterface:
    def do_something(self, input):
        return input  # Mocking the behavior

class DatabaseHelper:
    class JDBCtemplate:
        @staticmethod
        def batch_update(query):
            pass  # Mocking the behavior

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
