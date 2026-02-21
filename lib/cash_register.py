#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # The default discount value is 0
        self.discount = discount
        # The total starts at 0
        self.total = 0
        # List of all items added
        self.items = []

        # Tracks previous transactions and each transaction will be a dictionary
        self.previous_transactions = []

    # Discount Property
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Has to be an integer between 0 and 100 inclusive
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # Add Item
    def add_item(self, item, price, quantity=1):
        # Increase total
        self.total += price * quantity

        # Add individual items to the list
        for _ in range(quantity):
            self.items.append(item)

        # Save transactions
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # Apply the Discount
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Apply the percentage discount
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Remove the last transaction from history
        if self.previous_transactions:
            self.previous_transactions.pop()

        print(f"After the discount, the total comes to ${int(self.total)}.")

    # Void the last transaction
    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        # Subtract from the total
        self.total -= last["price"] * last["quantity"]

        # Remove items from items list
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])

          