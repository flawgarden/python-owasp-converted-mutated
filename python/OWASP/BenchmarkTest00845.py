
from flask import Flask, request, render_template
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/sqli-01/BenchmarkTest00845", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00845="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00845' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = unquote(param)

    bar = "This should never happen" if (7 * 42) - 106 > 200 else param

    sql = f"SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='{bar}'"
    try:
        conn = get_db_connection()
        results = conn.execute(sql).fetchall()
        conn.close()

        output = "Your results are: "
        for row in results:
            output += f"{row['USERNAME']} "
        return output
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
