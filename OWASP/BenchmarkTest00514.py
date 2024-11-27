
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00514", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class(content_type='text/html;charset=UTF-8')
        
        param = request.form.get('BenchmarkTest00514', '')

        bar = ''
        num = 106

        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

        try:
            conn, statement = get_sql_statement()
            statement.execute(sql)
            results = statement.fetchall()
            for row in results:
                response.response.append(str(row))
            conn.commit()
            statement.close()
            conn.close()
        except sqlite3.Error as e:
            response.response.append("Error processing request.")
            return response
        
        return response
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
