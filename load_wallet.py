"""load_wallet.py - LoadWallet class for managing a prepaid load balance."""


class LoadWallet:
    """A subscriber's prepaid load wallet."""

    SERVICE_CHARGE = 1.00  # flat fee (P) for sending to a different network

    def __init__(self, owner_name, mobile_number, starting_balance=0.0):
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.__balance = starting_balance  # private: only changed through methods

    @property
    def balance(self):
        """Read-only access to the private balance."""
        return self.__balance

    @staticmethod
    def is_valid_number(number):
        """A valid number has 11 digits and starts with 09 (e.g. 09171234567)."""
        return len(number) == 11 and number.isdigit() and number.startswith("09")

    def top_up(self, amount):
        """Add load to the wallet. Rejects zero or negative amounts."""
        if amount <= 0:
            print("Error: top-up amount must be greater than zero.")
            return False
        self.__balance += amount
        print(f"New balance: P{self.__balance:,.2f}")
        return True

    def send_load(self, amount, recipient_number):
        """Send load to another number on the SAME network (no fee)."""
        if not self.__can_send(amount, recipient_number, amount):
            return False
        self.__balance -= amount
        print(f"Sent P{amount:,.2f} to {recipient_number}.")
        print(f"New balance: P{self.__balance:,.2f}")
        return True

    def send_with_fee(self, amount, recipient_number):
        """Send load to a DIFFERENT network. A service charge is added."""
        total = amount + self.SERVICE_CHARGE
        if not self.__can_send(amount, recipient_number, total):
            return False
        self.__balance -= total
        print(f"Sent P{amount:,.2f} to {recipient_number}.")
        print(f"Service fee: P{self.SERVICE_CHARGE:,.2f}")
        print(f"New balance: P{self.__balance:,.2f}")
        return True

    def show_balance(self):
        """Display the owner's details and current balance."""
        print(f"Owner         : {self.owner_name}")
        print(f"Mobile Number : {self.mobile_number}")
        print(f"Balance       : P{self.__balance:,.2f}")

    # ---- private helper shared by both send methods ----
    def __can_send(self, amount, recipient_number, total_cost):
        if amount <= 0:
            print("Error: amount must be greater than zero.")
            return False
        if not self.is_valid_number(recipient_number):
            print("Error: invalid mobile number (use 11 digits, e.g. 09171234567).")
            return False
        if recipient_number == self.mobile_number:
            print("Error: you cannot send load to your own number.")
            return False
        if total_cost > self.__balance:
            print(f"Error: insufficient balance. You need P{total_cost:,.2f} "
                  f"but only have P{self.__balance:,.2f}.")
            return False
        return True
