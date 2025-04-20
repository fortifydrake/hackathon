import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def Model(transactions, income):
    # Extract data from transactions
    Date = []
    Category = []
    Amount = []

    for transaction in transactions:
        Date.append(transaction['date'])
        Category.append(transaction['category'])
        Amount.append(transaction['amount'])

    # Create a DataFrame
    df1 = pd.DataFrame({
        "Date": Date,
        "Category": Category,
        "Amount": Amount
    })

    print("Income:", income)
    print("Transactions DataFrame:\n", df1)

    # Validate DataFrame
    if df1.empty:
        print("No transactions available.")
        return {
            'savings': income,
            'savings_percentage': 100.0,
            'max_category': None,
            'max_amount': 0,
            'recommendations': "No transactions available to analyze.",
            'chart_url': None
        }

    # Ensure Amount column is numeric
    df1['Amount'] = pd.to_numeric(df1['Amount'], errors='coerce').fillna(0)

    # Calculate savings
    Samt = df1['Amount'].sum()
    print("Total Expenses (Samt):", Samt)

    saving = int(income - Samt)  # Convert to standard Python int
    sp = float((saving / income) * 100)  # Convert to standard Python float

    print("Savings:", saving)
    print("Savings Percentage:", sp)

    # Group data by category
    df2 = df1.groupby(['Category'])['Amount'].sum()
    if not df2.empty:
        max_category = df2.idxmax()
        max_amount = int(df2.max())  # Convert to standard Python int
    else:
        max_category = None
        max_amount = 0

    # Generate pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(df2, labels=df2.index, autopct='%1.1f%%')
    plt.title("Spending Breakdown by Category")
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    chart_url = base64.b64encode(img.getvalue()).decode()

    # Generate recommendations
    if max_category:
        recommendations = f"Your highest spending is on {max_category}. Consider reducing expenses in this category."
    else:
        recommendations = "No spending data available to generate recommendations."

    # Return results
    return {
        'savings': saving,
        'savings_percentage': sp,
        'max_category': max_category,
        'max_amount': max_amount,
        'recommendations': recommendations,
        'chart_url': f"data:image/png;base64,{chart_url}"
    }