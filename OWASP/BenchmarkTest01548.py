
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01548", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_text = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest01548", "")
    
    bar = Test().do_something(param)
    
    # Simulate setting session attribute
    with app.app_context():
        from flask import session
        session['userid'] = bar

    return f"Item: 'userid' with value: '{Utils.encode_for_html(bar)}' saved in session."

class Test:
    def do_something(self, param):
        guess = "ABC"
        switch_target = guess[2]
        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target == 'C' or switch_target == 'D':
            bar = param
        else:
            bar = "bobs_your_uncle"
        return bar

class Utils:
    @staticmethod
    def encode_for_html(value):
        # Simple HTML encoding function
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
