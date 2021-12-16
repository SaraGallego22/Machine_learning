def estimate_home_value(size_in_sqft, number_of_bedrooms):
    
    # Assume all homes are worth at least 50,000
    value = 50000

    # Adjust the value estimate based on the size of the house
    # Number of sqft por el valor de cada sqft + el value (lets suppouse that each sqtf cost 92 dollars)
    value = value + (size_in_sqft*  92)

    # Adjust the value estimate based on the number of bedrooms
    # Número de habitaciones por un valor adicional de nada habitación (Vamos a suponer que cada habitación vale 10000)
    value = value + (number_of_bedrooms * 10000)

    return value

# Estimate tha value of our house:
# - 5 bedrooms
# - 3800 sq ft
# Actual value: 450,000

value = estimate_home_value(3800, 5)

print("Estimated value:")
print(value)
