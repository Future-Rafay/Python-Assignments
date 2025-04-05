def main():
    fruit_prices: dict = {
        "apple": 200,
        "banana": 150,
        "orange": 400,
        "mango": 600,
        "watermelon": 150,
    }

    total_cost = 0

    print("Welcome to the Fruit Shop!")
    print("Enter quantity in kg for each fruit. Press Enter to skip.\n")

    for fruit, price in fruit_prices.items():
        print(f"{fruit} costs {price} Rs. per kg")
        quantity = input(f"How many kg of {fruit} do you want to buy? ")

        if quantity == "":
            print(f"Skipping {fruit}.\n")
            continue

        # Convert quantity to number and calculate cost
        try:
            kg = float(quantity)
            total_cost += kg * price
        except ValueError:
            print("Invalid input. Please enter a number.\n")

    print(f"\nYour total is Rs. {total_cost:.2f}")


if __name__ == '__main__':
    main()
