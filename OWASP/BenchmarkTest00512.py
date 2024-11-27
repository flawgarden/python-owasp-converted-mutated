
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00512", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    
    param = request.args.get('BenchmarkTest00512', '')

    bar = param
    
    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    
    try:
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            response.data += f"{row}<br>"
        
        connection.close()

    except Exception as e:
        response.data = "Error processing request."
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
