class VendingMachine:
    def __init__(self):
        self.menu = {
            "1": {"item": "Snickers Bar", "price": 1.50, "stock": 5},
            "2": {"item": "Water Bottle", "price": 1.00, "stock": 10},
            "3": {"item": "Sun Chips", "price": 2.00, "stock": 7},
            "4": {"item": "Cold Coffee", "price": 2.50, "stock": 5},
            "5": {"item": "Cheez-its", "price": 1.75, "stock": 8},
            "6": {"item": "Dr Pepper", "price": 1.25, "stock": 6},
            "7": {"item": "Goldfish Pretzels", "price": 1.80, "stock": 4},
            "8": {"item": "Honest Tea", "price": 2.20, "stock": 3}
        }
        self.money_inserted = 0.0
        self.total_change = 0.0

    def display_heading(self):
        print("""𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓔𝓵𝔀𝔂𝓷𝓷'𝓼 𝓥𝓮𝓷𝓭𝓲𝓷𝓰 𝓜𝓪𝓬𝓱𝓲𝓷𝓮""")

    def display_menu(self):
        print("\nMENU:")
        for code, item in self.menu.items():
            stock_status = "" if item["stock"] > 0 else "(Sold Out)"
            print(f"{code}: {item['item']} - ${item['price']:.2f} {stock_status}")

    def input_money(self):
        while True:
            try:
                self.money_inserted += float(input("Insert money: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def input_code(self):
        while True:
            code = input("Enter the code of the item you want to purchase (Type 'no' to stop): ").upper()
            if code == 'NO':
                return code
            if code in self.menu and self.menu[code]["stock"] > 0:
                return code
            elif code in self.menu and self.menu[code]["stock"] == 0:
                print("Sorry, this item is sold out. Please make another selection.")
            else:
                print("Invalid code. Please enter a valid code.")

    def dispense_item(self, item):
        print(f"\nDispensing {item}...")

    def calculate_change(self, money_inserted, item_price):
        return money_inserted - item_price

    def suggest_purchase(self, item):
        suggestions = {
            'Cold Coffee': 'How about adding a snack like Cheez-its?',
            'Honest Tea': 'Consider pairing it with Goldfish Pretzels.',
            'Cheez-its': 'Why not get a refreshing cup of Cold Coffee to go along with it',
            'Goldfish Pretzels': 'Give Honest Tea a try with it.'
        }
        return suggestions.get(item, '')

    def run(self):
        self.display_heading()
        self.display_menu()  # Display the menu first
        self.input_money()  # Ask the user to insert money after seeing the menu
        initial_money = self.money_inserted
        while True:
            code = self.input_code()
            if code == 'NO':
                break
            item = self.menu[code]
            price = item["price"]
            if self.money_inserted < price:
                print("Insufficient funds. Please insert more money.")
                break
            change = self.calculate_change(self.money_inserted, price)
            self.dispense_item(item["item"])
            self.total_change += change
            suggestion = self.suggest_purchase(item["item"])
            if suggestion:
                print(suggestion)
            item["stock"] -= 1
            if all(item["stock"] == 0 for item in self.menu.values()):
                print("Sorry, the vending machine is out of stock.")
                break
            self.money_inserted = change  # Use the remaining money for the next purchase
        remaining_money = self.money_inserted
        self.money_inserted = initial_money  # Reset money_inserted to the initial value
        print(f"Total change: ${remaining_money:.2f}")
        print("\nThank you for using the Vending Machine!")

# Run the vending machine
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
