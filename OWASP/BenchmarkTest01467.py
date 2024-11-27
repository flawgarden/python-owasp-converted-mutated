
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-03/BenchmarkTest01467", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    param = ""
    flag = True
    names = request.args

    for name in names:
        if flag:
            values = request.values.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest01467":
                        param = name
                        flag = False

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        conn = sqlite3.connect('database.db')  # Adjust the database name as needed
        cursor = conn.cursor()
        cursor.execute(sql)
        list_of_results = cursor.fetchall()
        cursor.close()
        conn.close()

        results_html = "Your results are: <br>"
        for result in list_of_results:
            results_html += f"{escape_html(str(result))}<br>"

        return results_html
    except Exception as e:
        return f"No results returned for query: {escape_html(sql)}"

class Test:

    def do_something(self, param):
        bar = "safe!"
        map34856 = {
            "keyA-34856": "a_Value",
            "keyB-34856": param,
            "keyC": "another_Value"
        }
        bar = map34856["keyB-34856"]
        bar = map34856["keyA-34856"]

        return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
