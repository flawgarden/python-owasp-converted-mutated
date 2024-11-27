
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02368", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02368":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        con = sqlite3.connect('database.db')  # Replace with your database configuration
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()
        return "Insert successful"
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    num = 106
    return "This_should_always_happen" if (7 * 18) + num > 200 else param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
