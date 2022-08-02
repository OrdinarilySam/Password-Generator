import random

class Password:

    # variables to check and store the password
    chars = ["abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789",
            " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]
    password = ""
    
    # initializes objects with parameters
    def __init__(self, length=12):
        self.length = length

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