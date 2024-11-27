
import base64
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect("database.db")
    return conn.cursor()

@app.route("/sqli-02/BenchmarkTest00938", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest00938')
    bar = ""

    if param is not None:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        for row in results:
            response.data += f"<p>{row}</p>"
    except sqlite3.Error as e:
        if True:  # Assumes hideSQLErrors is always True
            response.data = "Error processing request."
            return response
        else:
            raise e

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
