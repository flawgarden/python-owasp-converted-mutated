
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-01/BenchmarkTest00672", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get('BenchmarkTest00672', "")
        
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        sql = f"{{call {bar}}}"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql)
            results = statement.fetchall()
            return render_template("results.html", results=results, sql=sql)
        
        except sqlite3.Error as e:
            return "Error processing request."
    
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
