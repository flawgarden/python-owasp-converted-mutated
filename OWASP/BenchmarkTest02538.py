
from flask import Flask, request, render_template
import base64
from sqlalchemy import create_engine, text
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def do_something(param):
    a72634 = param
    b72634 = a72634 + " SafeStuff"
    b72634 = b72634[:-5] + "Chars"
    map72634 = {"key72634": b72634}
    c72634 = map72634["key72634"]
    d72634 = c72634[:-1]
    e72634 = base64.b64decode(base64.b64encode(d72634.encode())).decode()
    f72634 = e72634.split(" ")[0]
    # Here would be reflection or dynamic execution
    bar = "static_value"  # Hardcoded for safety
    return bar

@app.route("/sqli-05/BenchmarkTest02538", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.getlist("BenchmarkTest02538")[0] if request.form.getlist("BenchmarkTest02538") else ""
        bar = do_something(param)

        sql = f"SELECT USERNAME from USERS where USERNAME='foo' and PASSWORD='{bar}' LIMIT 1"
        try:
            engine = create_engine('sqlite:///database.db')  # Change to your database config
            with engine.connect() as connection:
                result = connection.execute(text(sql)).fetchone()
                response = result[0] if result else "No results returned"
            return render_template("result.html", results=response)
        except NoResultFound:
            return "No results returned for query"
        except SQLAlchemyError as e:
            return "Error processing request"

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
