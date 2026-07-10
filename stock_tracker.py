"""
Stock Portfolio Tracker
------------------------
Calculates total investment value based on manually defined stock prices.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 415,
    "AMZN": 185,
    "NFLX": 650,
    "META": 500,
}


def get_portfolio_input():
    """Ask the user for stock names and quantities, return as a dict."""
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Enter stock name and quantity (type 'done' to finish)\n")

    while True:
        stock = input("Stock symbol (or 'done'): ").strip().upper()
        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"  ⚠️  '{stock}' not found in price list. Try again.\n")
            continue

        qty_input = input(f"Quantity of {stock}: ").strip()
        try:
            qty = int(qty_input)
            if qty <= 0:
                print("  ⚠️  Quantity must be positive.\n")
                continue
        except ValueError:
            print("  ⚠️  Please enter a valid whole number.\n")
            continue

        # If stock already added, add to existing quantity
        portfolio[stock] = portfolio.get(stock, 0) + qty
        print(f"  ✅ Added {qty} shares of {stock}\n")

    return portfolio


def calculate_investment(portfolio):
    """Calculate per-stock value and total investment."""
    details = []
    total = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        total += value
        details.append({
            "stock": stock,
            "quantity": qty,
            "price": price,
            "value": value
        })
    return details, total


def display_summary(details, total):
    """Print a formatted summary table."""
    print("\n" + "=" * 45)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<12}")
    print("-" * 45)
    for item in details:
        print(f"{item['stock']:<8}{item['quantity']:<8}"
              f"${item['price']:<9}${item['value']:<11}")
    print("=" * 45)
    print(f"{'TOTAL INVESTMENT:':<26}${total:,.2f}")
    print("=" * 45)


def save_to_file(details, total):
    """Optionally save results to a .txt or .csv file."""
    choice = input("\nSave results to file? (txt/csv/no): ").strip().lower()

    if choice == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<12}\n")
            f.write("-" * 45 + "\n")
            for item in details:
                f.write(f"{item['stock']:<8}{item['quantity']:<8}"
                         f"${item['price']:<9}${item['value']:<11}\n")
            f.write("=" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")
        print(f"✅ Saved to {filename}")

    elif choice == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for item in details:
                writer.writerow([item["stock"], item["quantity"],
                                  item["price"], item["value"]])
            writer.writerow([])
            writer.writerow(["", "", "Total", total])
        print(f"✅ Saved to {filename}")

    else:
        print("Skipped saving.")


def main():
    print("📈 Welcome to the Stock Portfolio Tracker!\n")
    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    details, total = calculate_investment(portfolio)
    display_summary(details, total)
    save_to_file(details, total)


if __name__ == "__main__":
    main()
