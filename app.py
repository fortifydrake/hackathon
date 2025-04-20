from flask import Flask, request, jsonify, render_template
from my_budget_model import Model

app = Flask(__name__)

# Temporary storage for transactions
transactions = []

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/process', methods=['POST'])
def process_transactions():
    try:
        # Log the incoming request data
        data = request.json
        print("Received data:", data)

        # Extract income and transactions from the request
        income = data.get('income')
        new_transactions = data.get('transactions')

        # Validate the incoming data
        if not income or not new_transactions:
            return jsonify({"error": "Income or transactions missing"}), 400

        # Add new transactions to the global list
        global transactions
        transactions.extend(new_transactions)

        # Call the Model function
        result = Model(transactions, income)
        print("Model result:", result)

        # Return the result to the frontend
        return jsonify(result)
    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)