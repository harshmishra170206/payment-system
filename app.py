from flask import Flask, request
import uuid, datetime
app = Flask(__name__)

FORM = """<h2>Payment System v3</h2>
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
        rid = uuid.uuid4().hex[:8].upper()
        now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return f"<h3>Receipt {rid}</h3>Paid Rs {amount} on {now}. Payment successful."
    return FORM

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
