
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00760", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00760")
    param = values[0] if values else ""

    bar = "safe!"
    map18915 = {}
    map18915["keyA-18915"] = "a-Value"
    map18915["keyB-18915"] = param
    map18915["keyC"] = "another-Value"
    bar = map18915["keyB-18915"]

    sql = "{call " + bar + "}"

    try:
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            response.write(str(result))
        
        connection.close()

    except Exception as e:
        response.write("Error processing request.")
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
