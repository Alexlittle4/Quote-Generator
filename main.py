
#### `main.py`
```python
import random
import json
import os

QUOTES_FILE = "quotes.json"

def load_quotes():
    if os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, "r") as file:
            return json.load(file)
    return []

def save_quotes(quotes):
    with open(QUOTES_FILE, "w") as file:
        json.dump(quotes, file)

def add_quote(quotes):
    quote = input("Enter a new quote: ")
    quotes.append(quote)
    save_quotes(quotes)

def display_random_quote(quotes):
    if quotes:
        print(random.choice(quotes))
    else:
        print("No quotes available.")

def main():
    quotes = load_quotes()
    while True:
        print("\nQuote Generator")
        print("1. Add Quote")
        print("2. Display Random Quote")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_quote(quotes)
        elif choice == "2":
            display_random_quote(quotes)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
