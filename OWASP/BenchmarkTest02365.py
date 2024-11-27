
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02365", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            values = request.values.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest02365":
                        param = name
                        flag = False
                        break
            if not flag:
                break

        bar = do_something(param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            connection = sqlite3.connect('your_database.db')
            cursor = connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print_results(cursor, sql)
            connection.close()
        except sqlite3.Error as e:
            return "Error processing request.", 500

    return render_template("index.html")

def do_something(param):
    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value
    return bar

def print_results(cursor, sql):
    for row in cursor.fetchall():
        print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
