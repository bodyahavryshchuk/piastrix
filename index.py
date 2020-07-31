from flask import Flask, request, render_template, flash
import random
import loger

from piastrix import Piastrix

app = Flask(__name__)
app.secret_key = b'_5#fhg/iui54;xpga3]/'


@app.route('/')
def index():
    """Main page"""
    return render_template('main_form.html')


@app.route('/make_order', methods=['POST'])
def sendform():
    """Make order"""
    amount = request.form['amount']
    currency = request.form['currency']
    description = request.form['description']
    shop_order_id = random.randint(0, 1000000)
    p = Piastrix()
    if currency == '978':
        try:
            return p.pay(shop_order_id, currency, amount, description)
        except Exception as e:
            loger.save_log('pay: ERROR', e)
            flash('Error. Please try again')
            return render_template('main_form.html')
    elif currency == '840':
        try:
            return p.bill(shop_order_id, currency, amount, description)
        except Exception as e:
            loger.save_log('bill: ERROR', e)
            flash('Error. Please try again')
            return render_template('main_form.html')
    elif currency == '643':
        try:
            return p.invoice(shop_order_id, currency, amount, description)
        except Exception as e:
            loger.save_log('invoice: ERROR', e)
            flash('Error. Please try again')
            return render_template('main_form.html')


if __name__ == '__main__':
    app.run()
