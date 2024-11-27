
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00101", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("sqli-00/BenchmarkTest00101.html"))
        user_cookie = 'BenchmarkTest00101=bar; Max-Age=180; Secure; Path=' + request.path + '; Domain=' + request.host.split(':')[0]
        resp.set_cookie('BenchmarkTest00101', 'bar', max_age=180, secure=True, path=request.path)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00101' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00101'])

        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            statement = cursor.execute(sql, ("foo",))
            results = statement.fetchall()
            # Replace with function to print results
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
