import random

class Password:
    chars = {"lower":"abcdefghijklmnopqrstuvwxyz",
            "upper":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "numbers":"0123456789",
            "symbols":" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"}
    password = ""
    def __init__(self, lower=True, upper=True, nums=True, sym=True):
        self.lower = lower
        self.upper = upper
        self.nums = nums
        self.sym = sym

    def __str__(self):
        return f"Your password is {self.password}"

    @classmethod
    def generate(cls):
        ...

    def check(self):
        ...
    
    def create(self):
        ...


def main():
    password = Password().generate()
    print(password)

if __name__ == "__main__":
    main()