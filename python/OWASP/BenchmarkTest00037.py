
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00037", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = "<html><body>"
        param = ""
        flag = True
        names = request.form.keys()
        for name in names:
            values = request.form.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest00037":
                        param = name
                        flag = False
                        break

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + param + "'"

        try:
            connection = sqlite3.connect('your_database.db')
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            for row in results:
                response += str(row) + "<br>"
            connection.close()
        except sqlite3.DatabaseError as e:
            response += "Error processing request."
            return response

        response += "</body></html>"
        return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
