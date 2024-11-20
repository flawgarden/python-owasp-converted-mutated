
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name)

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-02/BenchmarkTest00939", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00939")

    bar = None
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    sql = "INSERT INTO users (username, password) VALUES ('foo','{}')".format(bar)

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        conn.commit()
        response.data = "Update complete."
        return response
    except sqlite3.Error as e:
        if True:  # Placeholder for hideSQLErrors
            response.data = "Error processing request."
            return response
        else:
            raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')
