def main():
    # Prompt the user to enter mass in kilograms
    mass_in_kg: float = float(input("Enter the mass in kilograms to calculate energy: "))

    # Speed of light in meters per second
    C: int = 299_792_458  # Underscores improve readability for large numbers

    # Calculate energy using Einstein's equation E = mc²
    energy: float = mass_in_kg * (C ** 2)

    # Display results
    print("\n--- Energy Calculation ---")
    print(f"Mass (m) = {mass_in_kg} kg")
    print(f"Speed of Light (c) = {C} m/s")
    print("Formula: E = mc²")
    print(f"Energy (E) = {energy:.2e} Joules")  # Display in scientific notation

if __name__ == "__main__":
    main()
