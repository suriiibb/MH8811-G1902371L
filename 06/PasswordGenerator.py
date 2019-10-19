#main program to print out 12 digit password
import random
def genPassword(n):
    password = []
    password += str(random.randint(0,9))
    password += random.choice('abcdefghijKLmnopqrstuvwxyz')
    password += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    password += random.choice("~!@#$%^&*()_+:\"<>?`-=,./;\'")
    all_chars = '0123456789abcdefghijKLmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+:\"<>?`-=,./;\''
    digit = len(all_chars) - 1
    for _ in range (n-4):
        index = random .randint(0,digit)
        password += all_chars[index]
    random.shuffle(password)
    password = ''.join(password)
    return password

if __name__ == "__main__":
    print (genPassword(12))

