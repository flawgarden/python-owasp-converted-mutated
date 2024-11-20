
from flask import Flask, request, make_response
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    # Assuming a SQLite database connection here for demonstration
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-01/BenchmarkTest00601", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    flag = True

    names = request.args.to_dict()
    for name, values in names.items():
        for value in values:
            if value == "BenchmarkTest00601":
                param = name
                flag = False
                break
        if not flag:
            break

    bar = ""
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        response.data = "Query executed successfully."
    except sqlite3.Error as e:
        response.data = "Error processing request."
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
