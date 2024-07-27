from jac_Lab9 import *
from lab9_decode import *

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    print("")
    choice = input("Please enter an option: ")
    return choice

if __name__ == '__main__':

    plain_text = ''
    cypher = ''
    rerun = True
    while rerun:
        choice = menu()
        if choice == '1':
            plain_text = input("Please enter your password to encode: ")
            cypher = encode(plain_text)
            print("Your password has been encoded and stored!")
            print("")
        if choice == '2':
            print("The encoded password is ", cypher, ", and the original password is ", decode(cypher), ".", sep="")
            print("")
        if choice == '3':
            rerun = False
