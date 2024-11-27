
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01465", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = ""
    flag = True

    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01465":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # DatabaseHelper.JDBCtemplate.execute(sql)  # Placeholder for actual execution
        encoded_sql = encode_for_html(sql)
        return f"No results can be displayed for query: {encoded_sql}<br> because the Spring execute method doesn't return results."

    except Exception as e:  # Placeholder for specific database exceptions
        return "Error processing request."

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def encode_for_html(value):
    # Placeholder for actual HTML encoding function
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
