
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Update with your database path
    return conn.cursor()

@app.route("/sqli-06/BenchmarkTest02740", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        param = request.form.get('BenchmarkTest02740')
        bar = do_something(param)

        sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

        try:
            statement = get_sql_statement()
            count = statement.execute(sql)
            response_data = "Update complete."
            statement.connection.commit()
            return response_data
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response
    return render_template("index.html")

def do_something(param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
