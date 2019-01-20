import pybase64
from colorama import init
init()
from colorama import Fore, Back
from sys import exit

def decode(base64):
    decode = ""
    while decode!= "y" or decode != "n":
        print(Fore.RESET)
        decode = input("Do you want to decode? (y/n): ")
        if decode == "y":
            print(Fore.CYAN, pybase64.b64decode(base64).decode("utf-8"))
            exit()
        elif decode == "n":
            exit()
        else:
            print(Fore.RED, "Invalid option! Please enter y or n")

def main():
    byteInput = input("Enter something to encode: ").encode()
    base64 = pybase64.b64encode(byteInput)
    string = base64.decode("utf-8")
    print(Fore.CYAN, 'base64 encoding: ', string)
    decode(base64)

main()