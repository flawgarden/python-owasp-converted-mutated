
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01315", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest01315', '')

    bar = Test().do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql, (bar,))
        conn.commit()
        output_update_complete(sql)
    except sqlite3.Error as e:
        if True:  # Replace with actual error handling condition
            return "Error processing request."
        else:
            raise e
    return ""

class Test:

    def do_something(self, param):
        # Simple ? condition that assigns constant to bar on true condition
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

def output_update_complete(sql):
    print(f"Executed SQL: {sql}")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
