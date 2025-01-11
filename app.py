# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/get_transactions')
def get_transactions():
    return render_template('transactions.html')

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']

        transaction = {
            'id': len(transactions) + 1,
            'date': date,
            'amount': amount
        }

        transactions.append(transaction)
        # print(transactions)
        return redirect(url_for('get_transactions'))

    return render_template('form.html')

# Update operation

# Delete operation

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)