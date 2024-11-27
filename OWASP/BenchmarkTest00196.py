
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00196", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00196', '')
    param = urllib.parse.unquote(param)

    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        # Simulate database execution (replace with actual DB code)
        # org.owasp.benchmark.helpers.DatabaseHelper.JDBCtemplate.execute(sql)
        return f"No results can be displayed for query: {sql}<br> because the Spring execute method doesn't return results."

    except Exception as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
