
# Function to normalize and calculate AQI
def normalize_and_calculate_aqi(conditions):
    normalized = {}
    for key in conditions:
        range_width = upper_limits[key] - lower_limits[key]
        normalized[key] = (conditions[key] - lower_limits[key]) / range_width if range_width != 0 else conditions[key]

    AQI = 1 - (normalized['CO2'] * weights['CO2'] + normalized['PM'] * weights['PM'] +
               normalized['VOCs'] * weights['VOCs'] + normalized['O3'] * weights['O3'] +
               (1 - normalized['O2']) * weights['O2'])

    AQI = max(0, min(AQI, 1))  # Ensure AQI is within [0, 1]
    return AQI


# Current weights setup
weights = {'O2': 0.12, 'CO2': 0.11, 'PM': 0.31, 'VOCs': 0.19, 'O3': 0.22, 'H2O': 0.05}

# Define the environmental scenarios
ideal_conditions = {'O2': 22, 'CO2': 200, 'PM': 0, 'VOCs': 0, 'O3': 0, 'H2O': 50}
poor_conditions = {'O2': 18, 'CO2': 2000, 'PM': 35, 'VOCs': 300, 'O3': 0.060, 'H2O': 30}

# Define lower and upper limits for each component
lower_limits = {'O2': 16, 'CO2': 0, 'PM': 0, 'VOCs': 0, 'O3': 0, 'H2O': 30}
upper_limits = {'O2': 23, 'CO2': 2000, 'PM': 35, 'VOCs': 300, 'O3': 0.060, 'H2O': 60}


# Calculate AQI for both scenarios
ideal_aqi = normalize_and_calculate_aqi(ideal_conditions)
poor_aqi = normalize_and_calculate_aqi(poor_conditions)

print(f"Ideal AQI: {ideal_aqi:.3f}, Poor AQI: {poor_aqi:.3f}\n")

####################################
# Real World Examples ##############
####################################

conditions_example_1 = {'O2': 23, 'CO2': 180, 'PM': 10, 'VOCs': 10, 'O3': 10, 'H2O': 60}
conditions_example_2 = {'O2': 22, 'CO2': 300, 'PM': 100, 'VOCs': 30, 'O3': 20, 'H2O': 40}
conditions_example_3 = {'O2': 23, 'CO2': 250, 'PM': 150, 'VOCs': 20, 'O3': 15, 'H2O': 50}
conditions_example_4 = {'O2': 24, 'CO2': 160, 'PM': 5, 'VOCs': 5, 'O3': 5, 'H2O': 70}
conditions_example_5 = {'O2': 22, 'CO2': 230, 'PM': 30, 'VOCs': 25, 'O3': 10, 'H2O': 60}

conditions_1_aqi = normalize_and_calculate_aqi(conditions_example_1)
print(f"Example 1 AQI: {conditions_1_aqi:.3f}")