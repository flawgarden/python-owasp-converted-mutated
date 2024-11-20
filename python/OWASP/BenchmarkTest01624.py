
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01624", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist("BenchmarkTest01624")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        try:
            sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
            # Assuming your JDBC template equivalent is implemented
            # DatabaseHelper.JDBCtemplate.batch_update(sql)
            return "No results can be displayed for query: " + sql + "<br>" + \
                   " because the batchUpdate method doesn't return results."
        except Exception as e:
            return "Error processing request."

    return render_template("index.html")

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
