from flask import Flask, request
app = Flask(__name__)

FORM = """<h2>Payment System v2</h2>
<form method='post'>
Name: <input name='name'><br>
Card No: <input name='card'><br>
Amount: <input name='amount'><br>
<button>Pay</button></form>"""

@app.route('/', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        card = request.form.get('card', '')
        amount = request.form.get('amount', '0')
        valid = False
        try:
            if card.isdigit() and len(card) == 16 and float(amount) > 0:
                valid = True
        except (ValueError, TypeError):
            valid = False
        if not valid:
            return "<h3>Invalid payment details</h3>" + FORM
        return "<h3>Details valid</h3>"
    return FORM

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
