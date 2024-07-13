import numpy as np


# Preprocessing functions for each component

def preprocess_O2(value):
    # Normalize O2 with a Gaussian-like function centered at 21%
    optimal_O2 = 21
    sigma = 1.0  # Adjust sigma for the desired gradient
    return np.exp(-((value - optimal_O2) ** 2) / (2 * sigma ** 2))


def preprocess_CO2(value):
    # Normalize CO2: optimal around 300 ppm, bad approaching 2500 ppm
    lower_limit = 300
    upper_limit = 2500
    if value <= lower_limit:
        return 1
    elif value >= upper_limit:
        return 0
    else:
        return max(0, min(1, 1 - (value - lower_limit) / (upper_limit - lower_limit)))


def preprocess_PM(value):
    # Normalize PM: optimal around 0 µg/m³, bad approaching 400 µg/m³
    upper_limit = 400
    return max(0, min(1, 1 - value / upper_limit))


def preprocess_VOCs(value):
    # Normalize VOCs: optimal around 0 µg/m³, bad approaching 1000 µg/m³
    upper_limit = 1000
    return max(0, min(1, 1 - value / upper_limit))


def preprocess_O3(value):
    # Normalize O3: optimal around 0 µg/m³, bad approaching 300 µg/m³
    upper_limit = 300
    return max(0, min(1, 1 - value / upper_limit))


def preprocess_H2O(value):
    # Normalize H2O: optimal relative humidity around 50%
    optimal_H2O = 50
    return max(0, min(1, 1 - abs(value - optimal_H2O) / optimal_H2O))


# Function to preprocess and weight the data
def preprocess_and_weight(component_data):
    component_weights = {'O2': 0.12, 'CO2': 0.11, 'PM': 0.31, 'VOCs': 0.19, 'O3': 0.22, 'H2O': 0.05}

    preprocessed_data = {
        'O2': preprocess_O2(component_data['O2']),
        'CO2': preprocess_CO2(component_data['CO2']),
        'PM': preprocess_PM(component_data['PM']),
        'VOCs': preprocess_VOCs(component_data['VOCs']),
        'O3': preprocess_O3(component_data['O3']),
        'H2O': preprocess_H2O(component_data['H2O'])
    }

    AQI = (
            preprocessed_data['O2'] * component_weights['O2'] +
            preprocessed_data['CO2'] * component_weights['CO2'] +
            preprocessed_data['PM'] * component_weights['PM'] +
            preprocessed_data['VOCs'] * component_weights['VOCs'] +
            preprocessed_data['O3'] * component_weights['O3'] +
            preprocessed_data['H2O'] * component_weights['H2O']
    )

    # Ensure AQI is between 0 and 1
    AQI = np.clip(AQI, 0, 1)

    return AQI, preprocessed_data


def calculate_AQI(input_conditions):
    AQI, _ = preprocess_and_weight(input_conditions)
    return AQI


# Define the new AQI categories with context
def map_AQI_to_category(aqi):
    if aqi < 0.35:
        return "Extremely bad. Acidic, Stress, Anxiety conditioner, Disease creating"
    elif aqi < 0.55:
        return "Bad. Disease exacerbating/sustaining (sensible groups)"
    elif aqi < 0.74:
        return "Moderate. Disease sustaining. Moderate body-mind functionality"
    elif aqi < 0.91:
        return "Good. Breathing becomes more free, nourishing, Inflammation drops, body starts slowly healing"
    else:
        return "Extremely Good. Healing air, full life/chemical sustaining of breath&body and natural functions"

