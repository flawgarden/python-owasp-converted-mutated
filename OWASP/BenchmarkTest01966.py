
from flask import Flask, request, render_template
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

engine = create_engine('sqlite:///database.db')  # Update with your database configuration

@app.route("/sqli-04/BenchmarkTest01966", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01966", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = f"SELECT USERNAME from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        with engine.connect() as connection:
            result = connection.execute(sql).fetchone()
            response_text = "Your results are: "
            response_text += result[0] if result else "No result found"
            return render_template("result.html", result=response_text)
    except NoResultFound:
        return render_template("result.html", result="No results returned for query.")
    except Exception as e:
        return render_template("error.html", error=str(e))

def do_something(param):
    num = 86
    if (7 * 42) - num > 200:
        return "This_should_always_happen"
    return param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
