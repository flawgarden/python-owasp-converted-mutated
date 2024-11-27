
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00519", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    map = request.form.to_dict()
    param = map.get("BenchmarkTest00519", "")

    bar = "safe!"
    map30190 = {
        "keyA-30190": "a_Value",
        "keyB-30190": param,
        "keyC": "another_Value"
    }

    bar = map30190["keyB-30190"]
    bar = map30190["keyA-30190"]

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        conn, cur = get_sql_statement()
        count = cur.execute(sql)
        conn.commit()
        conn.close()
        return render_template("success.html")  # assuming you have a success.html to show
    except sqlite3.Error as e:
        if True:  # replace with your condition to hide SQL errors
            response.data = b"Error processing request."
            return response
        else:
            raise Exception(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
