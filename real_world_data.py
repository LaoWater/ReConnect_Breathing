from processing_engine import calculate_AQI, map_AQI_to_category

# Define conditions for each scenario

# Scenario 1: At home, on the balcony, surrounded by greenery, after rain, 50m from the main road
conditions_example_1 = {
    'O2': 21,  # Normal oxygen levels
    'CO2': 500,  # Slightly above average due to nearby road
    'PM': 100,  # Reduced by rain, slight pollution from road
    'VOCs': 50,  # Low due to greenery & no cleaning/work
    'O3': 80,  # Low ozone levels
    'H2O': 70  # Higher humidity after rain
}

# Scenario 2: At the office, in the city center, sunny day
conditions_example_2 = {
    'O2': 20,  # Slightly Reduced oxygen due to indoors
    'CO2': 750,  # Elevated due to urban environment & indoors
    'PM': 180,  # Moderate particulate matter
    'VOCs': 250,  # Elevated due to city pollution
    'O3': 100,  # Higher due to sunny conditions
    'H2O': 40  # Moderate humidity
}

# Scenario 3: Walking in the park, near a construction area, sunny day, in the middle of the city
conditions_example_3 = {
    'O2': 21,  # Normal oxygen levels
    'CO2': 850,  # Elevated due to urban environment
    'PM': 280,  # High due to construction and traffic
    'VOCs': 200,  # Elevated due to urban environment
    'O3': 150,  # Moderate ozone levels
    'H2O': 48  # Normal humidity
}

# Scenario 4: In the middle of the forest, after a rainy day, a bit cool
conditions_example_4 = {
    'O2': 21,  # Normal oxygen levels
    'CO2': 350,  # Low due to high plant activity
    'PM': 10,  # Very low particulate matter
    'VOCs': 20,  # Very low due to natural environment
    'O3': 10,  # Very low ozone levels
    'H2O': 80  # High humidity after rain
}

# Scenario 5: In the city park, after rain, Sunday morning
conditions_example_5 = {
    'O2': 21,  # Normal oxygen levels
    'CO2': 500,  # Moderate due to reduced traffic
    'PM': 80,  # Reduced by rain but still present due to urban environment
    'VOCs': 100,  # Lower due to quiet morning
    'O3': 50,  # Low due to reduced sun activity and rain
    'H2O': 72  # High humidity after rain
}


# Scenario 6: City centre, sunny day, extraordinarily crowded, near construction site
conditions_example_6 = {
    'O2': 20,  # Slightly suboptimal
    'CO2': 700,  # Moderate due to traffic
    'PM': 340,  # Reduced by rain but still present due to urban environment
    'VOCs': 750,  # Higher
    'O3': 280,  # Low due to reduced sun activity and rain
    'H2O': 41  # High humidity after rain
}


# Calculate AQI and category for each scenario
def print_scenario_AQI(scenario_name, conditions):
    AQI = calculate_AQI(conditions)
    category = map_AQI_to_category(AQI)
    print(f"{scenario_name}")
    print(f"AQI: {AQI:.2f}")
    print(f"Air Quality Interpretation: {category}\n")


print_scenario_AQI("Scenario 6: City centre, sunny day, extraordinarily crowded, near construction site",
                   conditions_example_6)


# print_scenario_AQI("Scenario 2: At the office, in the city center, sunny day", conditions_example_2)
# print_scenario_AQI("Scenario 3: Walking in the park, near a construction area, sunny day,
# in the middle of the city", conditions_example_3)
# print_scenario_AQI("Scenario 4: In the middle of the forest, after a rainy day, a bit cool", conditions_example_4)
# print_scenario_AQI("Scenario 5: In the city, after rain, Sunday morning", conditions_example_5)
# print_scenario_AQI("Scenario 6: City centre, sunny day, extraordinarily crowded, near construction site",
# conditions_example_6)
