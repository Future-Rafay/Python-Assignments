"""
Milestone #2: Adding in All Planets

Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

"""
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Ask for user weight on Earth
    user_weight_on_earth_in_kg: float = float(input("Enter your Earth weight in kg: "))

    # List of valid planets
    valid_planets = {
        "mercury": MERCURY_GRAVITY,
        "venus": VENUS_GRAVITY,
        "mars": MARS_GRAVITY,
        "jupiter": JUPITER_GRAVITY,
        "saturn": SATURN_GRAVITY,
        "uranus": URANUS_GRAVITY,
        "neptune": NEPTUNE_GRAVITY,
        "earth": EARTH_GRAVITY
    }

    # Loop to ensure the user enters a valid planet
    while True:
        planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Earth): ").lower()
        
        # Check if the entered planet is valid
        if planet in valid_planets:
            planet_gravity = valid_planets[planet]
            # Calculate weight on the selected planet
            user_weight_on_planet_in_kg = user_weight_on_earth_in_kg * planet_gravity
            print(f"Your weight on {planet.capitalize()}: {user_weight_on_planet_in_kg:.2f} kg")
            break  # Exit the loop after valid input
        else:
            print("❌ Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()