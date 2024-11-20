
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01098", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.headers.get('BenchmarkTest01098', '')
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"
    
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.set_data("Error processing request.")
        return response
        
    return response

def output_update_complete(sql, response):
    response.set_data(f"Update complete: {sql}")
    
class Test:
    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
