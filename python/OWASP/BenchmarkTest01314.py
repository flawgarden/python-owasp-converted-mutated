
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01314", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01314", "")
        bar = Test().do_something(request, param)

        sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

        try:
            statement = database_con()  # Assume this returns a database connection
            cur = statement.execute(sql)
            statement.commit()  # Assuming you need to commit the changes
            output_update_complete(sql)
        except Exception as e:
            if hide_sql_errors:
                return "Error processing request."
            else:
                raise e

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

def database_con():
    import sqlite3
    return sqlite3.connect('your_database.db')  # Replace with your database connection details

def output_update_complete(sql):
    print(f"SQL Update Complete: {sql}")

hide_sql_errors = True  # Set this flag based on your needs

if __name__ == "__main__":
    app.run(host='0.0.0.0')
