# python einstein.py

# Constants
SPEED_OF_LIGHT = 300000000  # meters per second

# Function to calculate energy using Einstein's equation: E = mc^2
def calculate_energy(mass):
    energy = mass * SPEED_OF_LIGHT ** 2
    return energy

# Main function
def main():
    # Prompt the user for mass in kilograms
    mass = int(input("M: "))

    # Calculate the energy
    energy = calculate_energy(mass)

    # Output the equivalent energy in Joules
    print("E:", energy)

# Call the main function
if __name__ == "__main__":
    main()
