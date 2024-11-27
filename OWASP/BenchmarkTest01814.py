
from flask import Flask, request, render_template
from werkzeug.exceptions import InternalServerError
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:
    @staticmethod
    def query_for_row_set(sql):
        conn = sqlite3.connect('database.db')  # Adjust your database connection here
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except sqlite3.Error as e:
            raise InternalServerError(e)
        finally:
            conn.close()

class Test:
    def do_something(self, param):
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            return param
        elif switch_target == 'B':
            return "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            return param
        else:
            return "bobs_your_uncle"

@app.route("/sqli-04/BenchmarkTest01814", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01814')
        bar = Test().do_something(param)
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            results = DatabaseHelper.query_for_row_set(sql)
            response_content = "Your results are: "
            for row in results:
                response_content += str(row[0]) + " "
            return response_content
        except sqlite3.Error as e:
            return f"Error processing request: {str(e)}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
