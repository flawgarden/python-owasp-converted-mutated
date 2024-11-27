
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name)


def get_sql_connection():
    return sqlite3.connect('your_database.db')


@app.route("/sqli-01/BenchmarkTest00926", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = "text/html;charset=UTF-8"
    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00926")

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        # Logic to print results (you can customize how to display results)
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        response_content = "Error processing request."
        return response_content


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
