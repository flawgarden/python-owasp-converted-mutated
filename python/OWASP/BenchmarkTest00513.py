
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00513", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.form.get("BenchmarkTest00513", "")
        
        bar = "safe!"
        map63945 = {
            "keyA-63945": "a_Value",
            "keyB-63945": param,
            "keyC": "another_Value"
        }
        bar = map63945.get("keyB-63945", bar)
        bar = map63945.get("keyA-63945", bar)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            connection.close()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
