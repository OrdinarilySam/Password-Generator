from random import randint
import sys


length = 12 
all_special = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
special = ['!', '&', '%', '#', '^', '*', '@', '$']


chars = ["abcdefghijklmnopqrstuvwxyz",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "0123456789"]
chars.append(special)



def check_args():
    for arg in sys.argv:
        if arg.startswith("-x"):
            try:
                l = int(arg.lstrip("-x"))
                if l >= 4:
                    global length
                    length = int(l)
                else:
                    print("Specified length too short, using default")
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
        elif arg == "-c":
            chars.remove(special)
            check_special()
            chars.append(special)

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
            try:
                cat.index(char)
                valid = True
                break
            except ValueError:
                pass
        if not valid:
            return False
    return True

def check_special():
    print("The current special characters are:", special)
    print("Note: not all special characters will appear in the password\nType all for all special characters")
    chars = input("Which characters would you like to add/remove? ")
    if chars.lower().strip() == "all":
        special = all_special
        return
    for char in chars:
        try:
            special.pop(special.index(char))
        except ValueError:
            try:
                index = all_special.index(char)
                special.append(all_special[index])
            except ValueError:
                print(f"Character {char} not allowed")
    

def main():
    if len(sys.argv) >= 2:
        check_args()
    password = gen_password()
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()