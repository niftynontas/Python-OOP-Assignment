# Smartphone class (Base class)
class Smartphone:
    def __init__(self, brand, model, battery, os):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.os = os

    # Method to simulate a phone call
    def call(self):
        print(f"Calling... from {self.brand} {self.model}")

    # Method to simulate texting
    def text(self, message):
        print(f"Sending text: \"{message}\" from {self.brand} {self.model}")

    # Method to check battery status
    def battery_status(self):
        print(f"Battery at {self.battery}%")

# GamingSmartphone class (Subclass inheriting from Smartphone)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, os, gaming_mode=False):
        super().__init__(brand, model, battery, os)  # Call parent constructor
        self.gaming_mode = gaming_mode  # New attribute for gaming mode

    # Override the battery_status method for gaming smartphones
    def battery_status(self):
        battery_drain = self.battery - 20 if self.gaming_mode else self.battery
        print(f"Battery at {battery_drain}% (Gaming mode: {'ON' if self.gaming_mode else 'OFF'})")

    # New method to toggle gaming mode
    def toggle_gaming_mode(self):
        self.gaming_mode = not self.gaming_mode
        print(f"Gaming mode {'activated' if self.gaming_mode else 'deactivated'}.")

    # New method to simulate battery drain when in gaming mode
    def battery_drain_rate(self):
        if self.gaming_mode:
            self.battery -= 15  # higher battery drain
            print(f"Gaming mode on! Battery drained by 15%. Current battery: {self.battery}%")
        else:
            print("Gaming mode off, battery is stable.")

# Example usage:

# Create a regular Smartphone
my_phone = Smartphone("Apple", "iPhone 13", 80, "iOS")
my_phone.call()
my_phone.text("Hey, let's catch up later!")
my_phone.battery_status()

# Create a Gaming Smartphone
my_gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 100, "Android")
my_gaming_phone.call()
my_gaming_phone.toggle_gaming_mode()  # Activate gaming mode
my_gaming_phone.battery_status()  # Check battery
my_gaming_phone.battery_drain_rate()  # Simulate gaming mode battery drain
my_gaming_phone.battery_status()  # Check battery after drain
