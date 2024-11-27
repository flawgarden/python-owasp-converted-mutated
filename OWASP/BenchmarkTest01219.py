
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01219", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.get('BenchmarkTest01219')

    if headers:
        param = headers  # just grab the first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        connection = sqlite3.connect('database.db')  # Change to your database setup
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql, response)
    except sqlite3.DatabaseError as e:
        response.set_data("Error processing request.")
        return response
    
    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map23263 = {}
        map23263["keyA-23263"] = "a_Value"  # put some stuff in the collection
        map23263["keyB-23263"] = param  # put it in a collection
        map23263["keyC"] = "another_Value"  # put some stuff in the collection
        bar = map23263["keyB-23263"]  # get it back out
        bar = map23263["keyA-23263"]  # get safe value back out

        return bar

def print_results(rs, sql, response):
    # Custom logic to format and print results
    response.set_data(f"SQL Query: {sql}<br>Results: {rs}")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
