
import os
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

DATABASE_URL = 'sqlite:///yourdatabase.db'  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route("/sqli-05/BenchmarkTest02278", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02278", "")
        bar = do_something(param)

        sql = "SELECT userid FROM USERS WHERE USERNAME='foo' AND PASSWORD='{}'".format(bar)
        session = Session()
        try:
            result = session.execute(sql).scalar()
            return "Your results are: {}".format(result)
        except NoResultFound:
            return "No results returned for query: {}".format(sql)
        except Exception as e:
            return "Error processing request."

    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map96698 = {}
    map96698["keyA-96698"] = "a_Value"
    map96698["keyB-96698"] = param
    map96698["keyC"] = "another_Value"
    bar = map96698["keyB-96698"]
    bar = map96698["keyA-96698"]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
