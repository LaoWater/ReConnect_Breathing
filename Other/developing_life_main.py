class SystemDynamics:
    def __init__(self):
        self.karmic_balance = 100  # Initial karmic balance
        self.ks2_state = 'calm'  # Initial state of KS2
        self.default_programming_triggered = False
        self.trickster_engaged = False
        self.wisdom_in_action_enabled = False
        self.emotional_state = 'peaceful'  # Initial emotional state

    def update_karmic_balance(self, change):
        self.karmic_balance += change
        self.check_karmic_balance()

    def check_karmic_balance(self):
        if self.karmic_balance < 50:
            self.default_programming_triggered = True
            self.wisdom_in_action_enabled = False
        else:
            self.default_programming_triggered = False
            self.wisdom_in_action_enabled = True

    def engage_trickster(self):
        if self.default_programming_triggered:
            self.trickster_engaged = True
        else:
            self.trickster_engaged = False

    def eat_dhamma_aligned_food(self):
        if not self.trickster_engaged and self.wisdom_in_action_enabled:
            self.ks2_state = 'calm'
            print("Eating dhamma-aligned food.")
        else:
            self.ks2_state = 'inflamed'
            print("Default programming leads to non-dhamma food choices.")

    def sleep_and_reflect(self):
        if self.ks2_state == 'calm':
            print("Peaceful sleep and insightful reflections.")
        else:
            print("Sleep disturbed by KS2 discomfort.")

        # Adjust karmic balance based on reflections
        self.update_karmic_balance(10 if self.ks2_state == 'calm' else -10)

    def engage_in_mindful_practices(self):
        if self.wisdom_in_action_enabled:
            self.emotional_state = 'peaceful'
            print("Engaging in mindfulness and reflection.")
        else:
            self.emotional_state = 'turbulent'
            print("Struggling to maintain mindfulness.")

    def navigate_the_day(self):
        self.engage_trickster()
        self.eat_dhamma_aligned_food()
        self.sleep_and_reflect()
        self.engage_in_mindful_practices()


# Example of system dynamics over a day
system = SystemDynamics()
system.navigate_the_day()

# Example adjustments
system.update_karmic_balance(-20)  # A stressful event
system.navigate_the_day()
