
import os
from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02357", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest02357":
                    param = name
                    flag = False
                    break

    bar = do_something(request, param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        results = database_query(sql)
        return jsonify({"results": results})
    except Exception as e:
        if hide_sql_errors:
            return "Error processing request."
        else:
            return str(e), 500

def do_something(request, param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def database_query(sql):
    # Mocking database query. Replace with actual database query logic.
    return ["user1", "user2"]

hide_sql_errors = True

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
