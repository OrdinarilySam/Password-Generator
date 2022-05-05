from random import *

#global variables
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def main():
    print(gen_passwd(12))

def gen_passwd(length):
    valid = False
    string = lower  + upper + numbers + symbols
    while not valid:
        pwd = ""
        for i in range(length):
            pwd += pwd.join(string[randint(0,len(string)-1)])
        valid = check_passwd(pwd)
    return pwd

def check_passwd(pswd):
    pass

if __name__ == "__main__":
    main()
