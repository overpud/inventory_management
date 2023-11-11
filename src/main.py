class Transaction:
    def __init__(self, item_name, purchase_price, sold_price=None):
        self.item_name = item_name
        self.purchase_price = purchase_price
        self.sold_price = sold_price
        self.profit = None if sold_price is None else sold_price - purchase_price

    def update_sold_price(self, sold_price):
        self.sold_price = sold_price
        self.profit = sold_price - self.purchase_price

    def __str__(self):
        sold_price_str = "Unknown" if self.sold_price is None else f"{self.sold_price}"
        profit_str = "N/A" if self.profit is None else f"{self.profit}"
        return (f"Item: {self.item_name}, "
                f"Purchase Price: {self.purchase_price}, "
                f"Sold Price: {sold_price_str}, "
                f"Profit: {profit_str}")

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, item_name, purchase_price, sold_price=None):
        transaction = Transaction(item_name, purchase_price, sold_price)
        self.transactions.append(transaction)

    def update_transaction_sold_price(self, item_name, sold_price):
        for transaction in self.transactions:
            if transaction.item_name == item_name and transaction.sold_price is None:
                transaction.update_sold_price(sold_price)
                return True
        return False

    def calculate_yearly_revenue(self):
        return sum(t.profit for t in self.transactions if t.profit is not None)

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)

def main():
    tracker = FinanceTracker()

    while True:
        print("\nFinance Tracker")
        print("1. Add a transaction")
        print("2. Update sold price for a transaction")
        print("3. Show all transactions")
        print("4. Calculate yearly revenue")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            purchase_price = float(input("Enter purchase price: "))
            sold_price_input = input("Enter sold price (leave blank if unknown): ")
            sold_price = float(sold_price_input) if sold_price_input else None
            tracker.add_transaction(item_name, purchase_price, sold_price)
        elif choice == '2':
            item_name = input("Enter the item name to update: ")
            sold_price = float(input("Enter the new sold price: "))
            if not tracker.update_transaction_sold_price(item_name, sold_price):
                print("Item not found or sold price already set.")
        elif choice == '3':
            tracker.display_transactions()
        elif choice == '4':
            revenue = tracker.calculate_yearly_revenue()
            print(f"The yearly revenue is: {revenue}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
