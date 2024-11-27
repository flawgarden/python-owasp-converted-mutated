
import os
from flask import Flask, request, render_template, abort

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02536", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    else:
        return do_get(request)

def do_get(request):
    return do_post(request)

def do_post(request):
    response_text = ""
    values = request.args.getlist("BenchmarkTest02536")
    param = values[0] if values else ""

    bar = do_something(request, param)

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        
        # Assuming DatabaseHelper.JDBCtemplate.batchUpdate(sql) is defined in your application
        # org.owasp.benchmark.helpers.DatabaseHelper.JDBCtemplate.batchUpdate(sql)
        response_text += "No results can be displayed for query: " + encode_for_html(sql) + "<br>"
        response_text += " because the Spring batchUpdate method doesn't return results."
        return response_text
    except Exception as e:  
        return "Error processing request."

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def encode_for_html(sql):
    return sql.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
