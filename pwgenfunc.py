from random import randint
import sys

# Variables to be changed with sys args
length = 12 # -x[num] to change
special = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

chars = ["abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789"]
chars.append(special)

# def get_length():
#     while True:
#         try:
#             length = int(input("Password Length: ").strip())
#             return length
#         except ValueError:
#             pass

def check_args():
    for arg in sys.argv:
        if arg.startswith("-x"):
            try:
                l = int(arg.lstrip("-x"))
                if l >= 4:
                    global length
                    length = int(l)
            except ValueError:
                pass
        elif arg == "-l":
            chars.remove("abcdefghijklmnopqrstuvwxyz")
        elif arg == "-u":
            chars.remove("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif arg == "-n":
            chars.remove("0123456789")
        elif arg == "-s":
            chars.remove(special)

def gen_password():
    while True:
        password = ""
        for _ in range(length):
            cat = chars[randint(0,len(chars)-1)]
            char = cat[randint(0, len(cat)-1)]
            password += char
        if check_password(password):
            break 
    return password

def check_password(password):
    valid = False
    for cat in chars:
        valid = False
        for char in password:
            if cat.find(char) > -1:
                valid = True
                break
        if not valid:
            return False
    return True


def main():
    if len(sys.argv) >= 2:
        check_args()
    password = gen_password()
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()