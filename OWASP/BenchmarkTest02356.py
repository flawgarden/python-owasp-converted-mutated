
from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02356", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02356":
                    param = name
                    flag = False

    bar = do_something(param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Execute the SQL query
        # DatabaseHelper.JDBCtemplate.execute(sql) -- Placeholder for actual database execution
        print("No results can be displayed for query: " + sql)  # Simulate database interaction
        return "No results can be displayed for query: " + sql + "<br> because the execute method doesn't return results."
    
    except Exception as e:
        return "Error processing request."

def do_something(param):
    num = 196
    if (500 / 42) + num > 200:
        return param
    else:
        return "This should never happen"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
