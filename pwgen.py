import random

class Password:

    # variables to check and store the password
    chars = {"lower":"abcdefghijklmnopqrstuvwxyz",
            "upper":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "numbers":"0123456789",
            "symbols":" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"}
    password = ""
    
    # initializes objects with parameters
    def __init__(self, length=12, lower=True, upper=True, nums=True, sym=True):
        self.length = length
        self.lower = lower
        self.upper = upper
        self.nums = nums
        self.sym = sym

    # sets the value for when the object is called on 
    def __str__(self):
        return f"Your password is {self.password}"

    @classmethod
    def generate(cls):
        valid = False
        while not valid:
            ... #

    def check(self):
        ...
    

def main():
    password = Password().generate()
    print(password)

if __name__ == "__main__":
    main()