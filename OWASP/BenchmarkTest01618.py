
from flask import Flask, request, session, render_template
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'my_secret_key'

@app.route("/trustbound-00/BenchmarkTest01618", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        values = request.form.getlist('BenchmarkTest01618')
        param = values[0] if values else ""

        bar = Test().do_something(param)

        session['userid'] = bar

        return f"Item: 'userid' with value: '{html.escape(bar)}' saved in session."
    
    return render_template("index.html")

class Test:
    def do_something(self, param):
        thing = self.create_thing()
        bar = thing.do_something(param)
        return bar

    def create_thing(self):
        return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        # Placeholder for actual functionality
        return param 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
