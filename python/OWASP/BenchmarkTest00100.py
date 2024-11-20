
from flask import Flask, request, response, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00100", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = response.Response()
        user_cookie = response.set_cookie("BenchmarkTest00100", "bar", max_age=60*3, secure=True, path=request.path, domain=request.host)
        resp.headers.add('Set-Cookie', user_cookie)
        return render_template("sqli-00/BenchmarkTest00100.html")

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00100' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00100'])

        bar = "safe!"
        map72344 = {
            "keyA-72344": "a-Value",
            "keyB-72344": param,
            "keyC": "another-Value"
        }
        bar = map72344["keyB-72344"]

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('your_database.db')  # update with your database connection
            statement = connection.execute(sql, ("foo",))
            results = statement.fetchall()  # Get results
            return render_template("results.html", results=results)  # Assuming you have a template for showing results
        except sqlite3.Error as e:
            return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
