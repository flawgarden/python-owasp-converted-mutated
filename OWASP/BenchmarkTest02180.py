
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

DATABASE_URL = 'sqlite:///your_database.db'  # Change to your database URL
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@app.route("/sqli-04/BenchmarkTest02180", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02180', '')
        bar = do_something(param)
        sql = f"SELECT userid FROM USERS WHERE USERNAME='foo' AND PASSWORD='{bar}'"

        session = Session()
        try:
            result = session.execute(sql).fetchone()
            response_text = f"Your results are: {result[0]}"
        except NoResultFound:
            response_text = f"No results returned for query: {sql}"
        except Exception as e:
            response_text = "Error processing request."
            if not app.config.get('HIDE_SQL_ERRORS', False):
                raise e
        finally:
            session.close()

        return response_text
    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map32515 = {
        "keyA-32515": "a_Value",
        "keyB-32515": param,
        "keyC": "another_Value"
    }
    bar = map32515["keyB-32515"]
    bar = map32515["keyA-32515"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
