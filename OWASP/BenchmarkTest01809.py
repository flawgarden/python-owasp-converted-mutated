
import os
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
DATABASE_URL = 'sqlite:///database.db'  # Update with your database URL
engine = create_engine(DATABASE_URL)

@app.route("/sqli-03/BenchmarkTest01809", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01809', '')
        bar = Test().do_something(param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        try:
            with engine.connect() as connection:
                result = connection.execute(sql).fetchall()
                return "Your results are: <br>" + "<br>".join([str(row) for row in result])
        except NoResultFound:
            return f"No results returned for query: {sql}"
        except Exception as e:
            return "Error processing request."

    return render_template("index.html")

class Test:
    def do_something(self, param):
        a64594 = param
        b64594 = a64594 + " SafeStuff"
        b64594 = b64594[:-5] + "Chars"
        map64594 = {"key64594": b64594}
        c64594 = map64594["key64594"]
        d64594 = c64594[:-1]
        e64594 = b64decode(b64encode(d64594.encode())).decode()
        f64594 = e64594.split(" ")[0]

        thing = create_thing()  # Assuming this creates a thing-like object
        g64594 = "barbarians_at_the_gate"
        bar = thing.do_something(g64594)

        return bar

def create_thing():
    # Placeholder for creating a thing
    class Thing:
        def do_something(self, input):
            return input
    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
