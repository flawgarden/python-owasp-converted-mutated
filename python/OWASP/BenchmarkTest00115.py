
import os
import sqlite3
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-00/BenchmarkTest00115", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-00/BenchmarkTest00115.html"))
        user_cookie = make_response("bar")
        user_cookie.max_age = 60 * 3  # Store cookie for 3 minutes
        user_cookie.secure = True
        user_cookie.path = request.path
        response.set_cookie("BenchmarkTest00115", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if the_cookies:
            param = the_cookies.get("BenchmarkTest00115", param)

        bar = "safe!"
        map11928 = {
            "keyA-11928": "a-Value",
            "keyB-11928": param,
            "keyC": "another-Value"
        }
        bar = map11928.get("keyB-11928")

        sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql, (bar,))
            conn.commit()
            cursor.close()
            conn.close()
            return f"Update complete for SQL: {sql}"
        except sqlite3.Error as e:
            return "Error processing request."


if __name__ == "__main__":
    app.run(host='0.0.0.0')
