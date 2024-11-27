
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02176", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02176", "")
    bar = do_something(param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        execute_sql(sql)
        return "No results can be displayed for query: " + escape_html(sql) + "<br> because the execute method doesn't return results."

    except Exception as e:
        return "Error processing request."

def do_something(param):
    bar = param
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def execute_sql(sql):
    # Placeholder for your database execution logic.
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
