
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01471", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01471":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Here implement the database update logic
        # For example: DatabaseHelper.JDBCtemplate.batchUpdate(sql)
        return "No results can be displayed for query: " + sql + "<br> because the batchUpdate method doesn't return results."
    except Exception as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        bar = ""
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
