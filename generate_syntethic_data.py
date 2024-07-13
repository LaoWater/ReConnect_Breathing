import numpy as np
from processing_engine import calculate_AQI, preprocess_and_weight


def generate_synthetic_data(num_samples):
    synthetic_data = {}
    combined_data = []

    # Generate synthetic data for each component
    for component in lower_limits:
        synthetic_data[component] = np.random.randint(lower_limits[component], upper_limits[component] + 1, num_samples)

    # Preprocess each component and calculate AQI for each sample
    for i in range(num_samples):
        sample_data = {component: synthetic_data[component][i] for component in synthetic_data}
        AQI, _ = preprocess_and_weight(sample_data)
        combined_data.append(
            [sample_data['PM'], sample_data['O3'], sample_data['VOCs'], sample_data['CO2'], sample_data['O2'],
             sample_data['H2O'], AQI])

    return np.array(combined_data)


# Define lower and upper limits for each component
lower_limits = {'O2': 19, 'CO2': 0, 'PM': 0, 'VOCs': 0, 'O3': 0, 'H2O': 30}
upper_limits = {'O2': 23, 'CO2': 2500, 'PM': 400, 'VOCs': 1000, 'O3': 300, 'H2O': 80}

# Example of generating 100 samples
data = generate_synthetic_data(100)

print('Generated synthetic data')
header = "PM   O3   VOCs   CO2   O2  H2O  AQI"
print(header)
print("-" * len(header))
for row in data[:5]:
    print(
        f"{int(row[0]):3d} {int(row[1]):4d} {int(row[2]):5d} {int(row[3]):5d} {int(row[4]):4d} {int(row[5]):4d}"
        f" {row[6]:5.2f}")

# Example input conditions
conditions_example = {'O2': 20, 'CO2': 600, 'PM': 100, 'VOCs': 250, 'O3': 50, 'H2O': 65}

# Calculate AQI for the input conditions
AQI_value = calculate_AQI(conditions_example)
print("\nManual Conditions: ", conditions_example)
print(f"Calculated AQI: {AQI_value:.2f}")
