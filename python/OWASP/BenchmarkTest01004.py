
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route('/sqli-02/BenchmarkTest01004', methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest01004.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest01004=bar; Max-Age=180; Secure; Path=/sqli-02/BenchmarkTest01004; Domain=" + request.host)
        response.headers.add('Set-Cookie', user_cookie)
        return response
    else:
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01004' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01004'])

        bar = Test().do_something(request, param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            connection.commit()
            return render_template("results.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request."
 
class Test:
    def do_something(self, request, param):
        switch_target = 'C'
        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
