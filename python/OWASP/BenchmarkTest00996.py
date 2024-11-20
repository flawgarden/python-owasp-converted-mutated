
import base64
import sqlite3
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest00996", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest00996.html"))
        user_cookie = base64.b64encode(b"verifyUserPassword('foo','bar')").decode('utf-8')
        response.set_cookie("BenchmarkTest00996", user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response
    else:
        param = request.cookies.get("BenchmarkTest00996", "noCookieValueSupplied")
        bar = Test().do_something(param)

        sql = "{call " + bar + "}"

        try:
            connection = sqlite3.connect('database.db')  # Adjust with actual DB connection
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)  # Use rendering to display instead of print as required
            connection.close()

        except sqlite3.Error as e:
            return "Error processing request.", 500

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode('utf-8'))).decode('utf-8')
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
