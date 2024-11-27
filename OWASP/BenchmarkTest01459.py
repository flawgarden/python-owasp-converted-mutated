
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01459", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    param = ""
    flag = True

    for name in request.args.keys():
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01459":
                    param = name
                    flag = False
                    break
            if not flag:
                break

    bar = Test().do_something(request, param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('your_database.db')  # Replace with your database connection
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)  # Assuming a separate print_results function
        connection.close()

    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def print_results(results, sql):
    # Implement your logic to handle and print the results
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
