
from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

DATABASE_URI = 'sqlite:///yourdatabase.db'  # Update with your database URI
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@app.route("/sqli-03/BenchmarkTest01466", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ''
    flag = True

    for name in request.args.keys():
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == 'BenchmarkTest01466':
                    param = name
                    flag = False
                    break

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
    session = Session()

    try:
        results = session.execute(sql).fetchall()
        result_output = "Your results are: "
        for row in results:
            result_output += row['USERNAME'] + "<br>"
        return render_template("index.html", result=result_output)

    except NoResultFound:
        return render_template("index.html", result="No results returned for query: " + sql)
    except Exception as e:
        return render_template("index.html", result="Error processing request.")

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            del values_list[0]  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
