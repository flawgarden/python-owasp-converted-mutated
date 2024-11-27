
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01391", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01391', '')
        bar = Test().do_something(request, param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            statement = get_sql_statement()
            rs = statement.execute_query(sql)
            print_results(rs, sql)
        except Exception as e:
            if hide_sql_errors:
                return "Error processing request."
            else:
                raise e
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-24596": "a-Value",
            "keyB-24596": param,
            "keyC": "another-Value"
        }
        bar = map_["keyB-24596"]
        return bar

def get_sql_statement():
    # Placeholder for actual database connection and statement creation
    pass

def print_results(rs, sql):
    # Placeholder for result printing logic
    pass

hide_sql_errors = True  # Placeholder for error hiding logic

if __name__ == '__main__':
    app.run(host='0.0.0.0')
