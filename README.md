# Cellphone Load Wallet

A simple Python console application that simulates a prepaid mobile load wallet for managing balances, topping up credits, and sending load to other mobile numbers.

## Overview

This project models a prepaid wallet where a user can:

- create a wallet with an owner name and mobile number
- add balance through top-up
- send load to the same network without extra charges
- send load to another network with a service fee
- view the current wallet balance and account information

It is implemented in Python and can be run directly from the terminal.

## Features

- Validates mobile numbers using Philippine-style format (`09xxxxxxxxx`)
- Prevents invalid or zero/negative top-up amounts
- Blocks sending to your own number
- Checks for insufficient balance before transfer
- Applies a fixed service charge for cross-network transfers
- Keeps the wallet balance private and accessible through a property

## Project Structure

```text
Cellphone-Load-Wallet/
├── main.py          # Console menu and input handling
├── load_wallet.py   # Wallet logic and validation
└── README.md       # Project documentation
```

## Requirements

- Python 3.8 or newer

No external libraries are required.

## How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

## How It Works

When you start the program, it will prompt you for:

- owner name
- mobile number
- starting balance

After that, a menu appears with these choices:

1. Top Up Load
2. Send Load (same network)
3. Send Load (other network, with fee)
4. Show Balance
5. Exit

## Example

```text
Enter owner name: Juan Dela Cruz
Enter mobile number: 09171234567
Enter starting balance: 500

----- MENU -----
1. Top Up Load
2. Send Load (same network)
3. Send Load (other network, with fee)
4. Show Balance
5. Exit

Choose an option (1-5): 1
Enter top-up amount: 200
New balance: P700.00
```

## Validation Rules

- mobile number must be exactly 11 digits
- number must start with `09`
- top-up amount must be greater than zero
- load send amount must be greater than zero
- transfer cannot exceed available balance
- sending to the same number is not allowed

## Notes

This project is designed as a learning exercise for object-oriented programming in Python, especially around:

- classes and instances
- encapsulation
- validation logic
- menu-driven console applications

