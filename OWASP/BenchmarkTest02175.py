
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02175", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02175', '')
    bar = do_something(param)

    try:
        sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='" + bar + "'"
        # Assume a database execution method similar to JDBCtemplate.execute in the Java example
        execute_sql(sql)
        return "No results can be displayed for query: " + escape_html(sql) + "<br> because the execute method doesn't return results."
    except Exception as e:
        return "Error processing request."

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def execute_sql(sql):
    # Mock function to simulate SQL execution
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
