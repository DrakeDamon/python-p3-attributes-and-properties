APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.set_name(name)
        self.set_breed(breed)

    # Getter and Setter for Name
    def get_name(self):
        """The name getter method"""
        return self._name

    def set_name(self, name):
        '''Name must be string between 1 and 25 characters in length'''
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print(
                "Name must be string between 1 and 25 characters."
            )

    # Getter and Setter for Breed
    def get_breed(self):
        """The breed getter method"""
        return self._breed

    def set_breed(self, breed):
        """Breed must be in the list of approved breeds"""
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

# Usage
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)