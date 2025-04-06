"""
Milestone #1

Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MARS_MULTIPLE = 0.378

def main():
    user_weight_on_earth_in_kg: float = float(input("Enter your weight in kg: "))
    
    # Correct formula for weight on Mars (0.38 times Earth's weight)
    user_weight_on_mars_in_kg: float = user_weight_on_earth_in_kg * MARS_MULTIPLE
    
    print(f"The equivalent weight on Mars: {user_weight_on_mars_in_kg:.2f} kg")


if __name__ == "__main__":
    main()
