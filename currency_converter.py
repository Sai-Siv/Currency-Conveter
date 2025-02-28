import requests
def fetch_exchange_rates():
    api_url = "https://v6.exchangerate-api.com/v6/85bdfe6f5c478d9422ecff7c/latest/USD"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data.get('conversion_rates', {})
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch exchange rates: {e}")
        return {}

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    try:
        # Conversion calculation
        from_rate = exchange_rates[from_currency]
        to_rate = exchange_rates[to_currency]
        converted_amount = (amount / from_rate) * to_rate
        return converted_amount
    except KeyError:
        raise ValueError("Invalid currency code. Please check the input.")
    except Exception as e:
        raise ValueError(f"Conversion failed: {e}")

# Main function
def main():
    # Fetch exchange rates
    exchange_rates = fetch_exchange_rates()
    if not exchange_rates:
        print("Error: Unable to fetch exchange rates.")
        return

    # Display available currencies
    print("Available currencies:")
    print(", ".join(exchange_rates.keys()))

    try:
        # Get user input
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (e.g., USD): ").strip().upper()
        to_currency = input("Enter the currency to convert to (e.g., INR): ").strip().upper()

        # Perform conversion
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
        print(f"Converted Amount: {converted_amount:.5f} {to_currency}")
    except ValueError as e:
        print(f"Error: {e}")

# Run the program
if __name__ == "__main__":
    main()
