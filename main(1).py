"""main.py - Menu for the Cellphone Load Wallet. Run: python main.py"""

from load_wallet import LoadWallet


def ask_text(prompt):
    """Keep asking until the user types something."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def ask_amount(prompt, minimum=None):
    """Ask for an amount. Accepts '100', 'P100' or '1,000.50'."""
    while True:
        raw = input(prompt).strip().upper().replace("P", "").replace("₱", "").replace(",", "")
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a valid amount.")
            continue
        if minimum is not None and value < minimum:
            print(f"Amount must be at least {minimum}.")
            continue
        return value


def ask_mobile(prompt):
    """Keep asking until the user types a valid mobile number."""
    while True:
        number = input(prompt).strip()
        if LoadWallet.is_valid_number(number):
            return number
        print("Invalid number. Use 11 digits starting with 09 (e.g. 09171234567).")


def main():
    # ---- create the wallet ----
    name = ask_text("Enter owner name: ")
    number = ask_mobile("Enter mobile number: ")
    balance = ask_amount("Enter starting balance: ", 0)
    wallet = LoadWallet(name, number, balance)

    # ---- menu (shown once, as in the expected output) ----
    print("\n----- MENU -----")
    print("1. Top Up Load")
    print("2. Send Load (same network)")
    print("3. Send Load (other network, with fee)")
    print("4. Show Balance")
    print("5. Exit")

    while True:
        choice = input("\nChoose an option (1-5): ").strip()
        if choice == "1":
            wallet.top_up(ask_amount("Enter top-up amount: "))
        elif choice == "2":
            recipient = ask_mobile("Enter recipient number: ")
            wallet.send_load(ask_amount("Enter amount to send: "), recipient)
        elif choice == "3":
            recipient = ask_mobile("Enter recipient number: ")
            wallet.send_with_fee(ask_amount("Enter amount to send: "), recipient)
        elif choice == "4":
            wallet.show_balance()
        elif choice == "5":
            print("Thank you for using Load Wallet. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram ended.")
