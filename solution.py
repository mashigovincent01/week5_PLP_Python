# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand          # Public attribute
        self.model = model          # Public attribute
        self._storage = storage     # Protected attribute
        self.__battery = battery    # Private attribute

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def charge(self):
        print(f"Charging {self.model}'s battery...")

    # Getter for private attribute
    def get_battery(self):
        return f"Battery: {self.__battery}mAh"

    # Setter for private attribute
    def set_battery(self, new_battery):
        if new_battery > 0:
            self.__battery = new_battery
            print("Battery updated successfully!")

# Child Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system  # Additional attribute

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.model} with {self.cooling_system} cooling system!")

# Creating objects
phone = Smartphone("Samsung", "Galaxy S21", 128, 4000)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 6000, "Liquid Cooling")

# Using methods and accessing attributes
phone.make_call("123-456-7890")
print(phone.get_battery())
phone.charge()

gaming_phone.make_call("987-654-3210")
gaming_phone.play_game("Call of Duty")
print(gaming_phone.get_battery())
