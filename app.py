from flask import Flask, request
app = Flask(__name__)

FORM = """<h2>Payment System v1</h2>
<form method='post'>
Name: <input name='name'><br>
Card No: <input name='card'><br>
Amount: <input name='amount'><br>
<button>Pay</button></form>"""

@app.route('/', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        return f"<h3>Payment received for {request.form['name']}, Rs {request.form['amount']}</h3>"
    return FORM

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
